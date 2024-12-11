def markdown_to_blocks(markdown):
    strings = markdown.split('\n')
    map(lambda string: string.strip(), strings)
    return strings
     

