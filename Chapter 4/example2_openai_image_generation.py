import openai

openai.api_key = "YOUR_API_KEY"

def generate_image(prompt, num_images=1, size="1024x1024"):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=num_images,
            size=size
        )
        return [data['url'] for data in response['data']]
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

prompt = "A mobile phone displaying a customer support chatbot app interface"
image_urls = generate_image(prompt)

if image_urls:
    for url in image_urls:
        print(url)
