from metadata_parser import MetadataParser


def social_card_image(page_url):
    parser = MetadataParser(url=page_url, search_head_only=True)

    link = parser.get_metadata_link('image', strategy=['og'])

    return link
