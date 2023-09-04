from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailmarkdown.blocks import MarkdownBlock

class BodyStreamBlock(blocks.StreamBlock):
    h1 = blocks.CharBlock(label="Heading 1", icon="h1")
    h2 = blocks.CharBlock(label="Heading 2", icon="h2")
    h3 = blocks.CharBlock(label="Heading 3", icon="h3")
    paragraph = blocks.RichTextBlock(icon="draft")
    image = ImageChooserBlock(icon="image")
    
    markdown = MarkdownBlock(icon="code")