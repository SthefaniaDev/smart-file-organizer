from categories import CATEGORIES

def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    
    return "Outros"
        