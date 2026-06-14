package updater

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
	"time"
)

// CurrentVersion is the hardcoded version of the CLI
const CurrentVersion = "v1.0.0"

type githubRelease struct {
	TagName string `json:"tag_name"`
}

// CheckForUpdates asynchronously checks GitHub for a newer version
func CheckForUpdates() {
	client := http.Client{Timeout: 2 * time.Second}
	resp, err := client.Get("https://api.github.com/repos/fzihak/forma/releases/latest")
	if err != nil {
		return // Silently fail, don't interrupt the user
	}
	defer resp.Body.Close()

	var release githubRelease
	if err := json.NewDecoder(resp.Body).Decode(&release); err != nil {
		return
	}

	if release.TagName != "" && release.TagName != CurrentVersion {
		fmt.Println("\n" + strings.Repeat("=", 60))
		fmt.Printf("🚀 UPDATE AVAILABLE: Forma %s is out! (You are on %s)\n", release.TagName, CurrentVersion)
		fmt.Println("👉 Run 'npm update -g forma-cli' to upgrade to the latest Vanguard features.")
		fmt.Println(strings.Repeat("=", 60) + "\n")
	}
}
