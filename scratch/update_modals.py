import re

filePath = r"c:\Users\tinch\OneDrive\Desktop\weas\mio\sweet depyl\sitio web\index.html"

with open(filePath, "r", encoding="utf-8") as file:
    content = file.read()

# 1. Update the pel-variant-block container elements
# We want to change the divs matching:
# <div class="flex flex-col py-4 pel-variant-block" data-service-id="[SERVICE_ID]" data-name="[NAME]">
# to:
# <div class="flex flex-col py-3 px-3.5 my-1 rounded-lg border border-transparent cursor-pointer transition-all duration-200 pel-variant-block hover:bg-[#FDF4F8]/70 hover:border-[#E8D5CF]/50" data-service-id="[SERVICE_ID]" data-name="[NAME]" onclick="selectHairServiceBlock('[SERVICE_ID]', this)">

def repl_container(match):
    full_match = match.group(0)
    service_id = match.group(1)
    name = match.group(2)
    new_tag = f'<div class="flex flex-col py-3 px-3.5 my-1 rounded-lg border border-transparent cursor-pointer transition-all duration-200 pel-variant-block hover:bg-[#FDF4F8]/70 hover:border-[#E8D5CF]/50" data-service-id="{service_id}" data-name="{name}" onclick="selectHairServiceBlock(\'{service_id}\', this)">'
    return new_tag

content = re.sub(
    r'<div class="flex flex-col py-4 pel-variant-block"\s+data-service-id="([^"]+)"\s+data-name="([^"]+)">',
    repl_container,
    content
)

# 2. Update size buttons inside the blocks to stop propagation
# We change onclick="selectHairVariant(...)" to onclick="event.stopPropagation(); selectHairVariant(...)"
content = content.replace('onclick="selectHairVariant(', 'onclick="event.stopPropagation(); selectHairVariant(')

with open(filePath, "w", encoding="utf-8") as file:
    file.write(content)

print("HTML modifications for pel-variant-block containers and buttons applied successfully!")
