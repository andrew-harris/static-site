import re
from textnode import *
 
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    
    for node in old_nodes:
        # Only process TEXT type nodes
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
            
        # Check if this text contains the delimiter
        text = node.text
        if delimiter not in text:
            result.append(node)
            continue
            
        # Find the start and end of the delimited section
        start_index = text.find(delimiter)
        end_index = text.find(delimiter, start_index + len(delimiter))
        
        if end_index == -1:
            raise ValueError(f"Closing delimiter not found: {delimiter}")
            
        # Extract the three parts: before, delimited content, after
        before = text[:start_index]
        content = text[start_index + len(delimiter):end_index]
        after = text[end_index + len(delimiter):]
        
        # Add nodes to result
        if before:
            result.append(TextNode(before, TextType.TEXT))
        if content:
            result.append(TextNode(content, text_type))
        if after:
            result.append(TextNode(after, TextType.TEXT))
            
    return result

def extract_markdown_images(text):
    output = []
    alt_text = re.findall(r"\[(.*?)\]", text)
    image_text = re.findall(r"\((.*?)\)", text)
    for i in range(len(alt_text)):
        tup = (alt_text[i], image_text[i])
        output.append(tup)
    return output

def extract_markdown_links(text):
    output = []
    alt_text = re.findall(r"\[(.*?)\]", text)
    link_text = re.findall(r"\((.*?)\)", text)
    for i in range(len(alt_text)):
        tup = (alt_text[i], link_text[i])
        output.append(tup)
    return output



def split_nodes_image(old_nodes):
    result = []
    
    for old_node in old_nodes:
        # If not a text node, just add it and continue
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
            
        # Get all images from the text
        images = extract_markdown_images(old_node.text)
        
        # If no images, just add the original node
        if not images:
            result.append(old_node)
            continue
            
        # Process the text with images
        remaining_text = old_node.text

        
        for alt_text, url in images:
            # Find the image markdown in the text
            image_markdown = f"![{alt_text}]({url})"
            parts = remaining_text.split(image_markdown, 1)
            
            # Add text before image if it exists
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))
                
            # Add the image node
            result.append(TextNode(alt_text, TextType.IMAGE, url))
            
            # Update remaining text
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        
        # Add any remaining text after the last image
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
    
    return result



def split_nodes_link(old_nodes):

    result = []
    
    for old_node in old_nodes:

        # If not a text node, just add it and continue
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        # Get all images from the text
        links = extract_markdown_links(old_node.text)

        # If no images, just add the original node
        if not links:
            result.append(old_node)
            continue

        # Process the text with images
        remaining_text = old_node.text

        for alt_text, url in links:
            # Find the image markdown in the text
            link_markdown = f"![{alt_text}]({url})"
            parts = remaining_text.split(link_markdown, 1)
            
            # Add text before image if it exists
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))
                
            # Add the image node
            result.append(TextNode(alt_text, TextType.LINK, url))
            
            # Update remaining text
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        
        # Add any remaining text after the last image
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
    
    return result


