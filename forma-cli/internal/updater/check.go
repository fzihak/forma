package updater

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
	"time"
)

// CurrentVersion is the hardcoded version of the CLI
const CurrentVersion = "v1.1.0"

type githubRelease struct {
	TagName string `json:"tag_name"`
}

// GetLatestVersion fetches the latest release tag from GitHub
func GetLatestVersion() (string, error) {
	client := http.Client{Timeout: 3 * time.Second}
	resp, err := client.Get("https://api.github.com/repos/fzihak/forma/releases/latest")
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	var release githubRelease
	if err := json.NewDecoder(resp.Body).Decode(&release); err != nil {
		return "", err
	}
	return release.TagName, nil
}

// CheckForUpdates asynchronously checks GitHub for a newer version
func CheckForUpdates() {
	latest, err := GetLatestVersion()
	
	if err == nil && latest != "" && latest != CurrentVersion {
		fmt.Println("\n" + strings.Repeat("=", 60))
		fmt.Printf("🚀 UPDATE AVAILABLE: Forma %s is out! (You are on %s)\n", latest, CurrentVersion)
		fmt.Println("👉 Run 'forma update' to upgrade to the latest Vanguard features.")
		fmt.Println(strings.Repeat("=", 60) + "\n")
	}
}
