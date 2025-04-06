// backend/go_module/network_monitor.go

package main

import (
	"fmt"
	"log"
	"os"
	"strings"
	"time"

	"github.com/google/gopacket"
	"github.com/google/gopacket/pcap"
)

var (
	device       = "eth0" // Change to the correct interface name
	snapshot_len = int32(1024)
	promiscuous  = false
	timeout      = 30 * time.Second
	handle       *pcap.Handle
)

func logSuspiciousPacket(packetInfo string) {
	file, err := os.OpenFile("backend/go_module/threat_logs.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	logger := log.New(file, "THREAT: ", log.LstdFlags)
	logger.Println(packetInfo)
}

func main() {
	var err error
	handle, err = pcap.OpenLive(device, snapshot_len, promiscuous, timeout)
	if err != nil {
		log.Fatal(err)
	}
	defer handle.Close()

	packetSource := gopacket.NewPacketSource(handle, handle.LinkType())

	fmt.Println("Starting network traffic monitor...")

	for packet := range packetSource.Packets() {
		// Simulate detection (e.g., checking for suspicious IP or patterns)
		if strings.Contains(packet.String(), "malicious") {
			info := fmt.Sprintf("Suspicious packet captured: %s", packet.String())
			fmt.Println(info)
			logSuspiciousPacket(info)
		}
	}
}
