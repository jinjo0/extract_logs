package main

import (
    "fmt"
    "io"
    "os"
    "strings"
)

func main() {
    // Get the current directory
    currentDirectory, err := os.Getwd()
    if err != nil {
        fmt.Println("Error getting current directory:", err)
        return
    }

    // Open the output file for appending
    outputFile, err := os.OpenFile("data.notxt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
    if err != nil {
        fmt.Println("Error opening output file:", err)
        return
    }
    defer outputFile.Close()

    // List all .txt files in the current directory
    files, err := os.ReadDir(currentDirectory)
    if err != nil {
        fmt.Println("Error reading directory:", err)
        return
    }

    // Iterate through each .txt file
    for _, file := range files {
        if strings.HasSuffix(file.Name(), ".txt") {
            // Open the current .txt file
            txtFile, err := os.Open(file.Name())
            if err != nil {
                fmt.Println("Error opening file:", err)
                continue
            }
            defer txtFile.Close()

            // Create a buffer to read chunks of the file
            buffer := make([]byte, 4096) // Adjust the buffer size as needed
            for {
                // Read a chunk of the file
                bytesRead, err := txtFile.Read(buffer)
                if err != nil && err != io.EOF {
                    fmt.Println("Error reading file:", err)
                    break
                }
                if bytesRead == 0 {
                    break
                }

                // Search for the presence of "ohio" in the chunk
                if strings.Contains(string(buffer[:bytesRead]), "columbus") || strings.Contains(string(buffer[:bytesRead]), "ohio") {
                    // If found, write the chunk to the output file
                    _, err := outputFile.Write(buffer[:bytesRead])
                    if err != nil {
                        fmt.Println("Error writing to output file:", err)
                        break
                    }
                }
            }
        }
    }
}
