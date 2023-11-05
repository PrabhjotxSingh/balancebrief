import requests
from bs4 import BeautifulSoup

def extract_and_save_article(url, output_file):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the title and content
            title = soup.title.string
            content = ''
            for paragraph in soup.find_all('p'):
                content += paragraph.get_text() + '\n'
            
            # Save the title and content to a .txt file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(f'Title: {title}\n\n')
                file.write(content)
            
            print(f"Article extracted and saved to {output_file}")
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the news article: ")
    output_file = input("Enter the name of the output .txt file: ")
    
    extract_and_save_article(url, output_file)
