dic={}
def add_book(bookid,title):
    dic[bookid]=title
def remove_book(bookid):
    del dic[bookid]
def search_book(bookid):
    return dic[bookid] if bookid in dic else "Book not found"
def update_title(bookid,new_title):
    if bookid in dic:
        dic[bookid]=new_title
        return "Title updated"
    else:
        return "Book not found"
def display_books():
    for bookid,title in dic.items():
        print(f"{bookid}: {title}")

