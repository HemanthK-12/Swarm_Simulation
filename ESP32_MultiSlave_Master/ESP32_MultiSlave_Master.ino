#include <esp_now.h>
#include <WiFi.h>

#define NUMSLAVES 20
esp_now_peer_info_t slaves[NUMSLAVES] = {};
int SlaveCnt = 0;
#define CHANNEL 1
#define PRINTSCANRESULTS 0
void InitESPNow()
{
    WiFi.disconnect();
    if (esp_now_init() == ESP_OK)
    {
        Serial.println("ESPNow Init Success");
    }
    else
    {
        Serial.println("ESPNow Init Failed");
        ESP.restart();
    }
}
void ScanForSlave()
{
    int8_t scanResults = WiFi.scanNetworks();
    memset(slaves, 0, sizeof(slaves));
    SlaveCnt = 0;
    Serial.println("");
    if (scanResults == 0)
        Serial.println("No WiFi devices in AP Mode found");
    else
    {
        Serial.print("Found ");
        Serial.print(scanResults);
        Serial.println(" devices ");
        for (int i = 0; i < scanResults; ++i)
        {
            String SSID = WiFi.SSID(i);
            int32_t RSSI = WiFi.RSSI(i);
            String BSSIDstr = WiFi.BSSIDstr(i);
            if (PRINTSCANRESULTS)
            {
                Serial.print(i + 1);
                Serial.print(": ");
                Serial.print(SSID);
                Serial.print(" [");
                Serial.print(BSSIDstr);
                Serial.print("]");
                Serial.print(" (");
                Serial.print(RSSI);
                Serial.print(")");
                Serial.println("");
            }
            delay(10);
            if (SSID.indexOf("Slave") == 0)
            {
                Serial.print(i + 1);
                Serial.print(": ");
                Serial.print(SSID);
                Serial.print(" [");
                Serial.print(BSSIDstr);
                Serial.print("]");
                Serial.print(" (");
                Serial.print(RSSI);
                Serial.print(")");
                Serial.println("");
                int mac[6];
                if (6 == sscanf(BSSIDstr.c_str(), "%x:%x:%x:%x:%x:%x", &mac[0], &mac[1], &mac[2], &mac[3], &mac[4], &mac[5]))
                {
                    for (int ii = 0; ii < 6; ++ii)
                        slaves[SlaveCnt].peer_addr[ii] = (uint8_t)mac[ii];
                }
                slaves[SlaveCnt].channel = CHANNEL; // pick a channel
                slaves[SlaveCnt].encrypt = 0;       // no encryption
                SlaveCnt++;
            }
        }
    }

    if (SlaveCnt > 0)
    {
        Serial.print(SlaveCnt);
        Serial.println(" Slave(s) found, processing..");
    }
    else
        Serial.println("No Slave Found, trying again.");
    WiFi.scanDelete();
}
void manageSlave()
{
    if (SlaveCnt > 0)
    {
        for (int i = 0; i < SlaveCnt; i++)
        {
            Serial.print("Processing: ");
            for (int ii = 0; ii < 6; ++ii)
            {
                Serial.print((uint8_t)slaves[i].peer_addr[ii], HEX);
                if (ii != 5)
                    Serial.print(":");
            }
            Serial.print(" Status: ");
            bool exists = esp_now_is_peer_exist(slaves[i].peer_addr);
            if (exists)
                Serial.println("Already Paired");
            else
            {
                esp_err_t addStatus = esp_now_add_peer(&slaves[i]);
                if (addStatus == ESP_OK)
                    Serial.println("Pair success");
                else if (addStatus == ESP_ERR_ESPNOW_NOT_INIT)
                    Serial.println("ESPNOW Not Init");
                else if (addStatus == ESP_ERR_ESPNOW_ARG)
                    Serial.println("Add Peer - Invalid Argument");
                else if (addStatus == ESP_ERR_ESPNOW_FULL)
                    Serial.println("Peer list full");
                else if (addStatus == ESP_ERR_ESPNOW_NO_MEM)
                    Serial.println("Out of memory");
                else if (addStatus == ESP_ERR_ESPNOW_EXIST)
                    Serial.println("Peer Exists");
                else
                    Serial.println("Not sure what happened");
                delay(100);
            }
        }
    }
    else
        Serial.println("No Slave found to process");
}
uint8_t data = 0;
void sendData()
{
    data++;
    for (int i = 0; i < SlaveCnt; i++)
    {
        const uint8_t *peer_addr = slaves[i].peer_addr;
        if (i == 0)
        {
            Serial.print("Sending: ");
            Serial.println(data);
        }
        esp_err_t result = esp_now_send(peer_addr, &data, sizeof(data));
        Serial.print("Send Status: ");
        if (result == ESP_OK)
            Serial.println("Success");
        else if (result == ESP_ERR_ESPNOW_NOT_INIT)
            Serial.println("ESPNOW not Init.");
        else if (result == ESP_ERR_ESPNOW_ARG)
            Serial.println("Invalid Argument");
        else if (result == ESP_ERR_ESPNOW_INTERNAL)
            Serial.println("Internal Error");
        else if (result == ESP_ERR_ESPNOW_NO_MEM)
            Serial.println("ESP_ERR_ESPNOW_NO_MEM");
        else if (result == ESP_ERR_ESPNOW_NOT_FOUND)
            Serial.println("Peer not found.");
        else
            Serial.println("Not sure what happened");
        delay(100);
    }
}
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status)
{
    char macStr[18];
    snprintf(macStr, sizeof(macStr), "%02x:%02x:%02x:%02x:%02x:%02x",
             mac_addr[0], mac_addr[1], mac_addr[2], mac_addr[3], mac_addr[4], mac_addr[5]);
    Serial.print("Last Packet Sent to: ");
    Serial.println(macStr);
    Serial.print("Last Packet Send Status: ");
    Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}
void setup()
{
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);
    Serial.println("ESPNow/Multi-Slave/Master Example");
    Serial.print("STA MAC: ");
    Serial.println(WiFi.macAddress());
    InitESPNow();
    esp_now_register_send_cb(OnDataSent);
}
void loop()
{
    ScanForSlave();
    if (SlaveCnt > 0)
    {
        manageSlave();
        sendData();
    }
    else
       Serial.println("No slave found to process");
    delay(1000);
}
