import os
import re

# --- 1. THE TOOLS (Capabilities) ---
def list_wiki_topics():
    """Returns a list of all markdown files in the Wiki folder."""
    wiki_path = "./Wiki/"
    files = [f for f in os.listdir(wiki_path) if f.endswith('.md')]
    return [f.replace('.md', '') for f in files]

def extract_links(content):
    """Finds all [[Wikilinks]] in a given text and returns them as a list."""
    # This 'regular expression' looks for text inside double brackets [[...]]
    return re.findall(r'\[\[(.*?)\]\]', content)

def get_wiki_summary(topic):
    """Reads a wiki page and extracts only the content under '## Summary'."""
    file_path = f"./Wiki/{topic}.md"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "## Summary" in content:
                parts = content.split("## Summary")
                summary_plus_rest = parts[1]
                if "## " in summary_plus_rest:
                    summary = summary_plus_rest.split("## ")[0]
                else:
                    summary = summary_plus_rest
                return summary.strip()
            else:
                return "No '## Summary' section found."
    except FileNotFoundError:
        return None # Return None if the linked file doesn't exist yet

# --- 2. THE AGENT LOOP ---
def run_librarian_agent():
    print("--- Welcome to your Wiki 'Subject Map' Agent ---")
    
    while True:
        topics = list_wiki_topics()
        print(f"\nI found {len(topics)} topics in your Wiki:")
        
        # Display topics as a numbered list
        for i, topic in enumerate(topics, 1):
            print(f"  {i}. {topic}")

        raw_input = input("\nSelect a number or type a topic name (or 'exit'): ").strip()

        if raw_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Handle Number Selection
        selected_topic = None
        if raw_input.isdigit():
            index = int(raw_input) - 1
            if 0 <= index < len(topics):
                selected_topic = topics[index]
            else:
                print(f"Error: {raw_input} is not a valid number in the list.")
                continue
        else:
            # Handle Name Selection (Fallback)
            if raw_input in topics:
                selected_topic = raw_input
            else:
                print(f"I don't see '{raw_input}' in the list.")
                continue

        # If we have a valid selection, proceed to map it
        if selected_topic:
            print(f"\nAI is 'mapping' [[{selected_topic}]]...")
            file_path = f"./Wiki/{selected_topic}.md"
            with open(file_path, 'r', encoding='utf-8') as f:
                main_content = f.read()
            
            # Find all linked articles
            linked_topics = extract_links(main_content)
            
            # Fetch and display summaries for each link
            print(f"\nFound {len(linked_topics)} related articles in this topic:")
            print("=" * 40)
            
            # We'll store the clean links in a list so we can pick them by number later
            results_map = []
            for i, link in enumerate(linked_topics, 1):
                clean_link = link.split('|')[0] 
                results_map.append(clean_link)
                summary = get_wiki_summary(clean_link)
                
                print(f"  {i}. ARTICLE: [[{clean_link}]]")
                if summary:
                    print(f"     SUMMARY: {summary}")
                else:
                    print(f"     SUMMARY: (File not found or no Summary section)")
                print("-" * 20)
            
            print("=" * 40)

            # --- SUB-MENU: View Article or Return ---
            while True:
                print("\nWhat would you like to do next?")
                print("  [#] Type an article number to see the FULL content")
                print("  [B] Back to main topic list")
                sub_choice = input("Choice: ").strip().lower()

                if sub_choice == 'b':
                    break # Go back to the main topic list
                
                if sub_choice.isdigit():
                    sub_index = int(sub_choice) - 1
                    if 0 <= sub_index < len(results_map):
                        target_article = results_map[sub_index]
                        print(f"\n--- FULL CONTENT OF [[{target_article}]] ---")
                        try:
                            with open(f"./Wiki/{target_article}.md", 'r', encoding='utf-8') as f:
                                print(f.read())
                        except FileNotFoundError:
                            print(f"Error: Could not find the file for '{target_article}'.")
                        print("-" * 40)
                        input("\nPress Enter to return to the results menu...")
                    else:
                        print(f"Error: {sub_choice} is not a valid result number.")
                else:
                    print("Invalid choice. Type a number or 'B'.")

if __name__ == "__main__":
    run_librarian_agent()
