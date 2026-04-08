# Session Routine: Cloud-to-Local Sync

## Step 1: Sync from Drive
- Access the Google Drive folder: `1p8u_mfa7qtWy3WFTv3U41hEF8RsXkgD5` using the Workspace MCP.
- List all files in that folder.
- Download/Move all files from that Drive folder into the local `\Raw` directory.
- **Important:** Once a file is successfully moved to local storage, delete/trash the original from the Google Drive folder.


## Step 2: Process Raw Files
- Scan the local `\Raw` folder for any new content.
- **If a file is .png format:**
    - Use vision capabilities to extract all text, data, and technical specs.
    - If the PNG contains a diagram or sketch, describe the image detail.
    - Reformat the extracted content into a **Markdown (.md)** file.
    - Name the new file based on the article's title (e.g., `Gemma4_Guide.md`).
    - Keep a reference to the original image filename in the metadata of the .md file.
    - Move the .png file to the `\Archive` Folder.
- **If a file is Google Doc format:**  
    - Convert to .docx file.

## Step 3: Stop!!!! Don't do anything else.    