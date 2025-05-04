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

