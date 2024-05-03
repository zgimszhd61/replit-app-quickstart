from replit.object_storage import Client

client = Client()
client.download_as_text("hello.txt")
lists = client.list()
for item in lists:
    print(item)
