from textnode import TextNode

def main():
    node = TextNode(text="This is some anchor text", text_type="link", url="https://www.boot.dev")
    print(f"{node}")


main()