import tkinter
import sqlite3

conn=sqlite3.connect("ArtGallery.db")

def purchase_view():
    i = 100
    root24 = tkinter.Tk()
    root24.geometry('800x500')

    f24 = tkinter.Frame(root24, bg="#172c3e")
    f24.place(height=800, width=800)

    head1 = tkinter.Label(f24, text="CUSTOMER", fg='yellow', bg='#172c3e')
    head1.place(x=100, y=50)
    head2 = tkinter.Label(f24, text="ARTWORK", fg='yellow', bg='#172c3e')
    head2.place(x=300, y=50)
    head3 = tkinter.Label(f24, text="PRICE", fg='yellow', bg='#172c3e')
    head3.place(x=500, y=50)
    head4 = tkinter.Label(f24, text="DATE", fg='yellow', bg='#172c3e')
    head4.place(x=600, y=50)

    row = list(conn.execute("Select * from Purchase"))
    for r in row:
        a = r[0]
        b = r[1]
        c = r[2]
        d = r[3]

        one = tkinter.Label(f24, text=a, fg='yellow', bg='#172c3e')
        one.place(x=100, y=i)
        two = tkinter.Label(f24, text=b, fg='yellow', bg='#172c3e')
        two.place(x=300, y=i)
        three = tkinter.Label(f24, text=c, fg='yellow', bg='#172c3e')
        three.place(x=500, y=i)
        four = tkinter.Label(f24, text=d, fg='yellow', bg='#172c3e')
        four.place(x=600, y=i)
        i += 30

def customer_view():
    i = 100
    root24 = tkinter.Tk()
    root24.geometry('800x500')

    f24 = tkinter.Frame(root24, bg="#172c3e")
    f24.place(height=800, width=800)

    head1 = tkinter.Label(f24, text="NAME", fg='yellow', bg='#172c3e')
    head1.place(x=100, y=50)
    head2 = tkinter.Label(f24, text="ADDRESS", fg='yellow', bg='#172c3e')
    head2.place(x=300, y=50)
    head3 = tkinter.Label(f24, text="PHONE NO.", fg='yellow', bg='#172c3e')
    head3.place(x=500, y=50)
    head4 = tkinter.Label(f24, text="AMOUNT SPENT", fg='yellow', bg='#172c3e')
    head4.place(x=650, y=50)

    row = list(conn.execute("Select * from Customer order by CName ASC "))
    for r in row:
        a = r[0]
        b = r[1]
        c = r[2]
        d = r[3]

        one = tkinter.Label(f24, text=a, fg='yellow', bg='#172c3e')
        one.place(x=100, y=i)
        two = tkinter.Label(f24, text=b, fg='yellow', bg='#172c3e')
        two.place(x=300, y=i)
        three = tkinter.Label(f24, text=c, fg='yellow', bg='#172c3e')
        three.place(x=500, y=i)
        four = tkinter.Label(f24, text=d, fg='yellow', bg='#172c3e')
        four.place(x=650, y=i)
        i += 30

def artwork_view():
    i = 100
    root24 = tkinter.Tk()
    root24.geometry('800x500')

    f24 = tkinter.Frame(root24, bg="#172c3e")
    f24.place(height=800, width=800)

    head1 = tkinter.Label(f24, text="TITLE", fg='yellow', bg='#172c3e')
    head1.place(x=100, y=50)
    head2 = tkinter.Label(f24, text="ARTIST", fg='yellow', bg='#172c3e')
    head2.place(x=300, y=50)
    head3 = tkinter.Label(f24, text="YEAR", fg='yellow', bg='#172c3e')
    head3.place(x=500, y=50)
    head4 = tkinter.Label(f24, text="TYPE", fg='yellow', bg='#172c3e')
    head4.place(x=600, y=50)
    head5 = tkinter.Label(f24, text="PRICE", fg='yellow', bg='#172c3e')
    head5.place(x=700, y=50)

    row = list(conn.execute("Select * from ArtWork order by Title ASC"))
    for r in row:
        a = r[0]
        b = r[1]
        c = r[2]
        d = r[3]
        e = r[4]

        one = tkinter.Label(f24, text=a, fg='yellow', bg='#172c3e')
        one.place(x=100, y=i)
        two = tkinter.Label(f24, text=b, fg='yellow', bg='#172c3e')
        two.place(x=300, y=i)
        three = tkinter.Label(f24, text=c, fg='yellow', bg='#172c3e')
        three.place(x=500, y=i)
        four = tkinter.Label(f24, text=d, fg='yellow', bg='#172c3e')
        four.place(x=600, y=i)
        five = tkinter.Label(f24, text=e, fg='yellow', bg='#172c3e')
        five.place(x=700, y=i)
        i += 30

def artist_view():
    i = 100
    root24 = tkinter.Tk()
    root24.geometry('800x500')

    f24 = tkinter.Frame(root24, bg="#172c3e")
    f24.place(height=800, width=800)

    head1 = tkinter.Label(f24, text="ARTIST", fg='yellow', bg='#172c3e')
    head1.place(x=100, y=50)
    head2 = tkinter.Label(f24, text="AGE", fg='yellow', bg='#172c3e')
    head2.place(x=300, y=50)
    head3 = tkinter.Label(f24, text="BIRTHPLACE", fg='yellow', bg='#172c3e')
    head3.place(x=400, y=50)
    head4 = tkinter.Label(f24, text="STYLE", fg='yellow', bg='#172c3e')
    head4.place(x=500, y=50)

    row = list(conn.execute("Select * from Artist order by AName ASC"))
    for r in row:
        a = r[0]
        b = r[1]
        c = r[2]
        d = r[3]

        one = tkinter.Label(f24, text=a, fg='yellow', bg='#172c3e')
        one.place(x=100, y=i)
        two = tkinter.Label(f24, text=b, fg='yellow', bg='#172c3e')
        two.place(x=300, y=i)
        three = tkinter.Label(f24, text=c, fg='yellow', bg='#172c3e')
        three.place(x=400, y=i)
        four = tkinter.Label(f24, text=d, fg='yellow', bg='#172c3e')
        four.place(x=500, y=i)
        i += 30

def purchase_searchdata():
    i=150
    sum=0
    cname = purchase_searchbox.get()

    row = list(conn.execute("Select * from Purchase where CName=?", (cname,)))
    if len(row) == 0:
        del_fail = tkinter.Label(f12, text="Not Found                 ", fg='yellow', bg='#172c3e')
        del_fail.place(x=150, y=200)
    else:
        f_up = tkinter.Frame(root12, bg="#172c3e")
        f_up.place(height=800, width=800)

        success_label = tkinter.Label(f_up, text="Found", fg='yellow', bg='#172c3e')
        success_label.place(x=150, y=50)

        headtitle = tkinter.Label(f_up, text="ARTWORK", fg='yellow', bg='#172c3e')
        headtitle.place(x=100, y=100)
        headprice = tkinter.Label(f_up, text="PRICE", fg='yellow', bg='#172c3e')
        headprice.place(x=300, y=100)
        headdate = tkinter.Label(f_up, text="DATE", fg='yellow', bg='#172c3e')
        headdate.place(x=400, y=100)

        for r in row:
            a = r[1]
            b = r[2]
            c = r[3]

            name = tkinter.Label(f_up, text=a, fg='yellow', bg='#172c3e')
            name.place(x=100, y=i)
            price = tkinter.Label(f_up, text=b, fg='yellow', bg='#172c3e')
            price.place(x=300, y=i)
            date_label = tkinter.Label(f_up, text=c, fg='yellow', bg='#172c3e')
            date_label.place(x=400, y=i)
            sum+=int(b)
            i+=30

        total_label = tkinter.Label(f_up, text="Total amount spent on gallery : ", fg='yellow', bg='#172c3e')
        total_label.place(x=100, y=i)
        total = tkinter.Label(f_up, text=sum, fg='yellow', bg='#172c3e')
        total.place(x=300, y=i)

def customer_searchdata():
    cname = customer_searchbox.get()

    row = list(conn.execute("Select * from Customer where CName=?", (cname,)))
    for r in row:
        a = r[0]
        b = r[1]
        c = r[2]
        d = r[3]
    if len(row) == 0:
        del_fail = tkinter.Label(f11, text="Not Found                 ", fg='yellow', bg='#172c3e')
        del_fail.place(x=150, y=200)
    else:
        f_up = tkinter.Frame(root11, bg="#172c3e")
        f_up.place(height=400, width=400)

        success_label = tkinter.Label(f_up, text="Found", fg='yellow', bg='#172c3e')
        success_label.place(x=150, y=50)

        cname_label = tkinter.Label(f_up, text="Name:", fg='yellow', bg='#172c3e')
        cname_label.place(x=100, y=100)

        cname_textbox = tkinter.Label(f_up, text=a, fg='#7fff00', bg='#172c3e')
        cname_textbox.place(x=250, y=100)

        add_label = tkinter.Label(f_up, text="Address:", fg='yellow', bg='#172c3e')
        add_label.place(x=100, y=150)

        add_textbox = tkinter.Label(f_up, text=b, fg='#7fff00', bg='#172c3e')
        add_textbox.place(x=250, y=150)

        pno_label = tkinter.Label(f_up, text="Phone No.:", fg='yellow', bg='#172c3e')
        pno_label.place(x=100, y=200)

        pno_textbox = tkinter.Label(f_up, text=c, fg='#7fff00', bg='#172c3e')
        pno_textbox.place(x=250, y=200)

        amt_label = tkinter.Label(f_up, text="Total amount spent:", fg='yellow', bg='#172c3e')
        amt_label.place(x=100, y=250)

        amt_textbox = tkinter.Label(f_up, text=d, fg='#7fff00', bg='#172c3e')
        amt_textbox.place(x=250, y=250)

def artwork_searchdata():
    title = artwork_searchbox.get()

    row = list(conn.execute("Select * from ArtWork where Title=?", (title,)))
    for r in row:
        a = r[0]
        b = r[1]
        c = r[2]
        d = r[3]
        e = r[4]
    if len(row) == 0:
        del_fail = tkinter.Label(f10, text="Not Found                 ", fg='yellow', bg='#172c3e')
        del_fail.place(x=150, y=200)
    else:
        f_up = tkinter.Frame(root10, bg="#172c3e")
        f_up.place(height=400, width=400)

        success_label = tkinter.Label(f_up, text="Found", fg='yellow', bg='#172c3e')
        success_label.place(x=150, y=50)

        title_label = tkinter.Label(f_up, text="Title:", fg='yellow', bg='#172c3e')
        title_label.place(x=100, y=100)

        title_textbox = tkinter.Label(f_up, text=a, fg='#7fff00', bg='#172c3e')
        title_textbox.place(x=200, y=100)

        aname_label = tkinter.Label(f_up, text="Artist:", fg='yellow', bg='#172c3e')
        aname_label.place(x=100, y=150)

        aname_textbox = tkinter.Label(f_up, text=b, fg='#7fff00', bg='#172c3e')
        aname_textbox.place(x=200, y=150)

        year_label = tkinter.Label(f_up, text="Year:", fg='yellow', bg='#172c3e')
        year_label.place(x=100, y=200)

        year_textbox = tkinter.Label(f_up, text=c, fg='#7fff00', bg='#172c3e')
        year_textbox.place(x=200, y=200)

        type_label = tkinter.Label(f_up, text="Type:", fg='yellow', bg='#172c3e')
        type_label.place(x=100, y=250)

        type_textbox = tkinter.Label(f_up, text=d, fg='#7fff00', bg='#172c3e')
        type_textbox.place(x=200, y=250)

        price_label = tkinter.Label(f_up, text="Price:", fg='yellow', bg='#172c3e')
        price_label.place(x=100, y=250)

        price_textbox = tkinter.Label(f_up, text=e, fg='#7fff00', bg='#172c3e')
        price_textbox.place(x=200, y=250)


def artist_searchdata():
    aname = artist_searchbox.get()

    row = list(conn.execute("Select * from Artist where AName=?", (aname,)))
    for r in row:
        a = r[0]
        b = r[1]
        c = r[2]
        d = r[3]
    if len(row) == 0:
        del_fail = tkinter.Label(f9, text="Not Found                 ", fg='yellow', bg='#172c3e')
        del_fail.place(x=150, y=200)
    else:
        f_up = tkinter.Frame(root9, bg="#172c3e")
        f_up.place(height=400, width=400)

        success_label = tkinter.Label(f_up, text="Found", fg='yellow', bg='#172c3e')
        success_label.place(x=150, y=50)

        aname_label = tkinter.Label(f_up, text="Name:", fg='yellow', bg='#172c3e')
        aname_label.place(x=100, y=100)

        aname_textbox = tkinter.Label(f_up, text=a, fg='#7fff00', bg='#172c3e')
        aname_textbox.place(x=200, y=100)

        age_label = tkinter.Label(f_up, text="Age:", fg='yellow', bg='#172c3e')
        age_label.place(x=100, y=150)

        age_textbox = tkinter.Label(f_up, text=b, fg='#7fff00', bg='#172c3e')
        age_textbox.place(x=200, y=150)

        bplace_label = tkinter.Label(f_up, text="Birthplace:", fg='yellow', bg='#172c3e')
        bplace_label.place(x=100, y=200)

        bplace_textbox = tkinter.Label(f_up, text=c, fg='#7fff00', bg='#172c3e')
        bplace_textbox.place(x=200, y=200)

        style_label = tkinter.Label(f_up, text="Style:", fg='yellow', bg='#172c3e')
        style_label.place(x=100, y=250)

        style_textbox = tkinter.Label(f_up, text=d, fg='#7fff00', bg='#172c3e')
        style_textbox.place(x=200, y=250)

def update_success3():
    conn.execute("UPDATE Customer set Cname=?, Address=?, Pno=? where Cname=?",  \
                (cname_textbox.get(), add_textbox.get(), pno_textbox.get(), cname))
    conn.commit()
    inserted = tkinter.Label(f_up , text="Data Updated Sucessfully", fg='yellow', bg='#172c3e')
    inserted.place(x=130, y=300)

def customer_up():
    global cname_textbox, add_textbox, pno_textbox, f_up, cname
    cname = customer_updatebox.get()

    row = list(conn.execute("Select * from Customer where CNAme=?", (cname,)))
    for r in row:
        a=r[0]
        b=r[1]
        c=r[2]
    if len(row) == 0:
        del_fail = tkinter.Label(f21, text="Not Found                 ", fg='yellow', bg='#172c3e')
        del_fail.place(x=150, y=200)
    else:
        f_up = tkinter.Frame(root21, bg="#172c3e")
        f_up.place(height=400, width=400)

        success_label = tkinter.Label(f_up, text="Found", fg='yellow', bg='#172c3e')
        success_label.place(x=150, y=50)

        cname_label = tkinter.Label(f_up, text="Name:", fg='yellow', bg='#172c3e')
        cname_label.place(x=100, y=100)

        cname_textbox = tkinter.Entry(f_up)
        cname_textbox.place(x=200, y=100)
        cname_textbox.insert(0, a)

        add_label = tkinter.Label(f_up, text="Address:", fg='yellow', bg='#172c3e')
        add_label.place(x=100, y=150)

        add_textbox = tkinter.Entry(f_up)
        add_textbox.place(x=200, y=150)
        add_textbox.insert(0, b)

        pno_label = tkinter.Label(f_up, text="Phone No.:", fg='yellow', bg='#172c3e')
        pno_label.place(x=100, y=200)

        pno_textbox = tkinter.Entry(f_up)
        pno_textbox.place(x=200, y=200)
        pno_textbox.insert(0, c)

        submit = tkinter.Button(f_up, text="Submit", command=update_success3)
        submit.place(x=150, y=250)



def update_success2():
    conn.execute("UPDATE ArtWork set Title=?, Aname=?, Year=?, Type=?, Price=? where Title=?",  \
                 (title_textbox.get(), aname_textbox.get(), yr_textbox.get(), type_textbox.get(), price_textbox.get(), title))
    conn.commit()
    inserted = tkinter.Label(f_up , text="Data Updated Sucessfully", fg='yellow', bg='#172c3e')
    inserted.place(x=130, y=400)

def artwork_up():
    global title_textbox, yr_textbox, aname_textbox, price_textbox, type_textbox, f_up, title
    title = artwork_updatebox.get()

    row = list(conn.execute("Select * from ArtWork where Title=?", (title,)))
    for r in row:
        a=r[0]
        b=r[1]
        c=r[2]
        d=r[3]
        e=r[4]
    if len(row) == 0:
        del_fail = tkinter.Label(f20, text="Not Found                 ", fg='yellow', bg='#172c3e')
        del_fail.place(x=150, y=200)
    else:
        f_up = tkinter.Frame(root20, bg="#172c3e")
        f_up.place(height=500, width=500)

        success_label = tkinter.Label(f_up, text="Found", fg='yellow', bg='#172c3e')
        success_label.place(x=150, y=50)

        title_label = tkinter.Label(f_up, text="Title:", fg='yellow', bg='#172c3e')
        title_label.place(x=100, y=100)

        title_textbox = tkinter.Entry(f_up)
        title_textbox.place(x=200, y=100)
        title_textbox.insert(0, a)

        aname_label = tkinter.Label(f_up, text="Artist:", fg='yellow', bg='#172c3e')
        aname_label.place(x=100, y=150)

        aname_textbox = tkinter.Entry(f_up)
        aname_textbox.place(x=200, y=150)
        aname_textbox.insert(0, b)

        yr_label = tkinter.Label(f_up, text="Year:", fg='yellow', bg='#172c3e')
        yr_label.place(x=100, y=200)

        yr_textbox = tkinter.Entry(f_up)
        yr_textbox.place(x=200, y=200)
        yr_textbox.insert(0, c)

        type_label = tkinter.Label(f_up, text="Style:", fg='yellow', bg='#172c3e')
        type_label.place(x=100, y=250)

        type_textbox = tkinter.Entry(f_up)
        type_textbox.place(x=200, y=250)
        type_textbox.insert(0, d)

        price_label = tkinter.Label(f_up, text="Price:", fg='yellow', bg='#172c3e')
        price_label.place(x=100, y=300)

        price_textbox = tkinter.Entry(f_up)
        price_textbox.place(x=200, y=300)
        price_textbox.insert(0, e)

        submit = tkinter.Button(f_up, text="Submit", command=update_success2)
        submit.place(x=150, y=350)


def update_success1():
    conn.execute("UPDATE Artist set Aname=?, Age=?, Birthplace=?, Style=? where Aname=?",  \
                 (aname_textbox.get(), age_textbox.get(), bplace_textbox.get(), style_textbox.get(), aname))
    conn.commit()
    inserted = tkinter.Label(f_up , text="Data Updated Sucessfully", fg='yellow', bg='#172c3e')
    inserted.place(x=130, y=350)

def artist_up():
    global aname_textbox, age_textbox, bplace_textbox, style_textbox, f_up, aname
    aname = artist_updatebox.get()

    row = list(conn.execute("Select * from Artist where AName=?", (aname,)))
    for r in row:
        a=r[0]
        b=r[1]
        c=r[2]
        d=r[3]
    if len(row) == 0:
        del_fail = tkinter.Label(f19, text="Not Found                 ", fg='yellow', bg='#172c3e')
        del_fail.place(x=150, y=200)
    else:
        f_up = tkinter.Frame(root19, bg="#172c3e")
        f_up.place(height=400, width=400)

        success_label = tkinter.Label(f_up, text="Found", fg='yellow', bg='#172c3e')
        success_label.place(x=150, y=50)
        aname_label = tkinter.Label(f_up, text="Name:", fg='yellow', bg='#172c3e')
        aname_label.place(x=100, y=100)

        aname_textbox = tkinter.Entry(f_up)
        aname_textbox.place(x=200, y=100)
        aname_textbox.insert(0, a)

        age_label = tkinter.Label(f_up, text="Age:", fg='yellow', bg='#172c3e')
        age_label.place(x=100, y=150)

        age_textbox = tkinter.Entry(f_up)
        age_textbox.place(x=200, y=150)
        age_textbox.insert(0, b)

        bplace_label = tkinter.Label(f_up, text="Birthplace:", fg='yellow', bg='#172c3e')
        bplace_label.place(x=100, y=200)

        bplace_textbox = tkinter.Entry(f_up)
        bplace_textbox.place(x=200, y=200)
        bplace_textbox.insert(0, c)

        style_label = tkinter.Label(f_up, text="Style:", fg='yellow', bg='#172c3e')
        style_label.place(x=100, y=250)

        style_textbox = tkinter.Entry(f_up)
        style_textbox.place(x=200, y=250)
        style_textbox.insert(0, d)

        submit = tkinter.Button(f_up, text="Submit", command=update_success1)
        submit.place(x=150, y=300)


def customer_del():
    cname = customer_deletebox.get()

    e = list(conn.execute("Select * from Customer where CName=?", (cname,)))
    if len(e) == 0:
        del_fail = tkinter.Label(f16, text="Not Found                 ", fg='yellow', bg='#172c3e')
        del_fail.place(x=130, y=200)
    else:
        conn.execute('DELETE FROM Customer WHERE CName=?', (cname,))
        conn.commit()
        deleted = tkinter.Label(f16, text="Data Deleted Sucessfully", fg='yellow', bg='#172c3e')
        deleted.place(x=100, y=200)

def artwork_del():
    title = artwork_deletebox.get()

    e = list(conn.execute("Select * from Artwork where Title=?", (title,)))
    if len(e) == 0:
        del_fail = tkinter.Label(f15, text="Not Found                 ", fg='yellow', bg='#172c3e')
        del_fail.place(x=130, y=200)
    else:
        conn.execute('DELETE FROM Artwork WHERE Title=?', (title,))
        conn.commit()
        deleted = tkinter.Label(f15, text="Data Deleted Sucessfully", fg='yellow', bg='#172c3e')
        deleted.place(x=100, y=200)

def artist_del():
    aname = artist_deletebox.get()

    e = list(conn.execute("Select * from Artist where AName=?", (aname,)))
    if len(e) == 0:
        del_fail = tkinter.Label(f14, text="Not Found                 ", fg='yellow', bg='#172c3e')
        del_fail.place(x=130, y=200)
    else:
        conn.execute('DELETE FROM Artist WHERE AName=?', (aname,))
        conn.commit()
        deleted = tkinter.Label(f14, text="Data Deleted Sucessfully", fg='yellow', bg='#172c3e')
        deleted.place(x=100, y=200)


def purchase_insert():
    cname = cname_textbox.get()
    title = title_textbox.get()
    pr = int(price_textbox.get())
    date = date_textbox.get()
    conn.execute(" INSERT INTO Purchase VALUES(?,?,?,?)", (cname, title, pr, date))
    conn.commit()
    #DELETING THE ARTWORK
    conn.execute("DELETE FROM ArtWork where Title = ?", (title,))
    conn.commit()
    #UPDATING IN CUSTOMER ALSO:
    row = list(conn.execute("Select * from Customer where CName=?", (cname,)))
    if len(row) == 0:
       conn.execute("INSERT INTO Customer (Cname, Amount) VALUES(?,?)", (cname, pr))
       conn.commit()
    else:
       for r in row:
            pr+= r[3]
       conn.execute("UPDATE Customer set Amount=? where Cname=?", (pr, cname))
       conn.commit()
    inserted = tkinter.Label(f6 , text="Data Inserted Sucessfully\nIf you're a new customer, please update your details"\
    , fg='yellow', bg='#172c3e')
    inserted.place(x=70, y=350)

def customer_insert():
    cname = cname_textbox.get()
    address = address_textbox.get()
    pno = pno_textbox.get()
    conn.execute("INSERT INTO Customer (CName, Address, Pno) VALUES(?,?, ?)", (cname, address, pno))
    conn.commit()
    inserted = tkinter.Label(f5 , text="Data Inserted Sucessfully", fg='yellow', bg='#172c3e')
    inserted.place(x=150, y=300)

def artwork_insert():
    title = title_textbox.get()
    aname = aname_textbox.get()
    yr = yr_textbox.get()
    type = type_textbox.get()
    cost = cost_textbox.get()
    conn.execute("INSERT INTO ArtWork VALUES(?,?,?,?,?)", (title, aname, yr, type, cost))
    conn.commit()
    inserted = tkinter.Label(f4 , text="Data Inserted Sucessfully", fg='yellow', bg='#172c3e')
    inserted.place(x=170, y=400)

def artist_insert():
    aname = aname_textbox.get()
    age = age_textbox.get()
    bplace = bplace_textbox.get()
    style = style_textbox.get()
    conn.execute("INSERT INTO Artist VALUES(?,?,?,?)", (aname, age, bplace, style))
    conn.commit()
    inserted = tkinter.Label(f3 , text="Data Inserted Sucessfully", fg='yellow', bg='#172c3e')
    inserted.place(x=150, y=350)



#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#



def artist_click():
    global root3, f3, aname_textbox, age_textbox, bplace_textbox, style_textbox, message
    root3 = tkinter.Tk()
    root3.geometry('400x600')

    f3 = tkinter.Frame(root3, bg="#172c3e")
    f3.place(height=600, width=400)

    enter_label = tkinter.Label(f3, text="Enter Artist Details:", fg='yellow', bg='#172c3e')
    enter_label.place(x=100, y=50)

    aname_label = tkinter.Label(f3, text="Name:", fg='yellow', bg='#172c3e')
    aname_label.place(x=50, y=100)

    aname_textbox = tkinter.Entry(f3)
    aname_textbox.place(x=150, y=100)

    age_label = tkinter.Label(f3, text="Age:", fg='yellow', bg='#172c3e')
    age_label.place(x=50, y=150)

    age_textbox = tkinter.Entry(f3)
    age_textbox.place(x=150, y=150)

    bplace_label = tkinter.Label(f3, text="Birthplace:", fg='yellow', bg='#172c3e')
    bplace_label.place(x=50, y=200)

    bplace_textbox = tkinter.Entry(f3)
    bplace_textbox.place(x=150, y=200)

    style_label = tkinter.Label(f3, text="Style:", fg='yellow', bg='#172c3e')
    style_label.place(x=50, y=250)

    style_textbox = tkinter.Entry(f3)
    style_textbox.place(x=150, y=250)

    submit = tkinter.Button(f3, text="Submit", command = artist_insert)
    submit.place(x=180, y=300)

    root3.mainloop()


def artwork_click():
    global root4, f4, title_textbox, aname_textbox, yr_textbox, type_textbox, cost_textbox
    root4 = tkinter.Tk()
    root4.geometry('400x600')

    f4 = tkinter.Frame(root4, bg="#172c3e")
    f4.place(height=600, width=400)

    enter_label = tkinter.Label(f4, text="Enter Artwork Details:", fg='yellow', bg='#172c3e')
    enter_label.place(x=100, y=50)

    title_label = tkinter.Label(f4, text="Artwork Name:", fg='yellow', bg='#172c3e')
    title_label.place(x=50, y=100)

    title_textbox = tkinter.Entry(f4)
    title_textbox.place(x=170, y=100)

    aname_label = tkinter.Label(f4, text="Artist Name:", fg='yellow', bg='#172c3e')
    aname_label.place(x=50, y=150)

    aname_textbox = tkinter.Entry(f4)
    aname_textbox.place(x=170, y=150)

    yr_label = tkinter.Label(f4, text="Year:", fg='yellow', bg='#172c3e')
    yr_label.place(x=50, y=200)

    yr_textbox = tkinter.Entry(f4)
    yr_textbox.place(x=170, y=200)

    type_label = tkinter.Label(f4, text="Type:", fg='yellow', bg='#172c3e')
    type_label.place(x=50, y=250)

    type_textbox = tkinter.Entry(f4)
    type_textbox.place(x=170, y=250)

    cost_label = tkinter.Label(f4, text="Cost:", fg='yellow', bg='#172c3e')
    cost_label.place(x=50, y=300)

    cost_textbox = tkinter.Entry(f4)
    cost_textbox.place(x=170, y=300)

    submit = tkinter.Button(f4, text="Submit", command=artwork_insert)
    submit.place(x=200, y=350)

    root4.mainloop()

def customer_click():
    global root5, f5, cname_textbox, address_textbox, pno_textbox
    root5 = tkinter.Tk()
    root5.geometry('400x600')

    f5 = tkinter.Frame(root5, bg="#172c3e")
    f5.place(height=600, width=400)

    enter_label = tkinter.Label(f5, text="Enter Customer Details:", fg='yellow', bg='#172c3e')
    enter_label.place(x=100, y=50)

    cname_label = tkinter.Label(f5, text="Name:", fg='yellow', bg='#172c3e')
    cname_label.place(x=50, y=100)

    cname_textbox = tkinter.Entry(f5)
    cname_textbox.place(x=150, y=100)

    address_label = tkinter.Label(f5, text="Address:", fg='yellow', bg='#172c3e')
    address_label.place(x=50, y=150)

    address_textbox = tkinter.Entry(f5)
    address_textbox.place(x=150, y=150)

    pno_label = tkinter.Label(f5, text="P No.:", fg='yellow', bg='#172c3e')
    pno_label.place(x=50, y=200)

    pno_textbox = tkinter.Entry(f5)
    pno_textbox.place(x=150, y=200)

    submit = tkinter.Button(f5, text="Submit", command=customer_insert)
    submit.place(x=180, y=250)

    root5.mainloop()

def purchase_click():
    global root6, f6, cname_textbox, price_textbox, title_textbox, date_textbox
    root6 = tkinter.Tk()
    root6.geometry('500x600')

    f6 = tkinter.Frame(root6, bg="#172c3e")
    f6.place(height=1000, width=1000)

    enter_label = tkinter.Label(f6, text="Enter Purchase Details:", fg='yellow', bg='#172c3e')
    enter_label.place(x=100, y=50)

    cname_label = tkinter.Label(f6, text="Name:", fg='yellow', bg='#172c3e')
    cname_label.place(x=50, y=100)

    cname_textbox = tkinter.Entry(f6)
    cname_textbox.place(x=170, y=100)

    title_label = tkinter.Label(f6, text="Artwork Title:", fg='yellow', bg='#172c3e')
    title_label.place(x=50, y=150)

    title_textbox = tkinter.Entry(f6)
    title_textbox.place(x=170, y=150)

    price_label = tkinter.Label(f6, text="Price:", fg='yellow', bg='#172c3e')
    price_label.place(x=50, y=200)

    price_textbox = tkinter.Entry(f6)
    price_textbox.place(x=170, y=200)

    date_label = tkinter.Label(f6, text="Date dd/mm/yy:", fg='yellow', bg='#172c3e')
    date_label.place(x=50, y=250)

    date_textbox = tkinter.Entry(f6)
    date_textbox.place(x=170, y=250)

    submit = tkinter.Button(f6, text="Submit", command=purchase_insert)
    submit.place(x=200, y=300)


    root6.mainloop()


def view_menu():

    root23 = tkinter.Tk()
    root23.geometry('700x300')

    f23 = tkinter.Frame(root23, bg="#172c3e")
    f23.place(height=1000, width=1000)

    welcome_label = tkinter.Label(f23, text="Welcome to Art Gallery", font = 'Calibri 21' , fg='#FF5722', bg='#172c3e')
    welcome_label.place(x=100, y=50)

    choice_label = tkinter.Label(f23, text="Please select from the options below:", fg='yellow', bg='#172c3e')
    choice_label.place(x=100, y=100)

    artist_button = tkinter.Button(f23, text="Artists", command=artist_view)
    artist_button.place(x=100, y=150)

    artwork_button = tkinter.Button(f23, text="Artworks", command=artwork_view)
    artwork_button.place(x=230, y=150)

    cust_button = tkinter.Button(f23, text="Customers", command=customer_view)
    cust_button.place(x=360, y=150)

    purchase_button = tkinter.Button(f23, text="Purchase History", command=purchase_view, width=13)
    purchase_button.place(x=490, y=150)

    root23.mainloop()


def func1():
    print("Hello")

def main_menu():
    root7 = tkinter.Tk()
    root7.geometry('600x400')

    f7 = tkinter.Frame(root7, bg="#172c3e")
    f7.place(height=1000, width=1000)

    welcome_label = tkinter.Label(f7, text="Welcome to Art Gallery", font = 'Calibri 21' , fg='#FF5722', bg='#172c3e')
    welcome_label.place(x=100, y=50)

    choice_label = tkinter.Label(f7, text="Choose an option:", fg='yellow', bg='#172c3e')
    choice_label.place(x=100, y=100)

    ins_button = tkinter.Button(f7, text="Insert Data", command=insert_menu, width=15)
    ins_button.place(x=100, y=150)

    del_button = tkinter.Button(f7, text="Delete Data", command=delete_menu, width=15)
    del_button.place(x=300, y=150)

    upd_button = tkinter.Button(f7, text="Update Data", command=update_menu, width=15)
    upd_button.place(x=100, y=200)

    search_button = tkinter.Button(f7, text="Search Data", command=search_menu, width=15)
    search_button.place(x=300, y=200)

    purchase_button = tkinter.Button(f7, text="Buy an Art Work", command=purchase_click, width=15)
    purchase_button.place(x=100, y=250)

    view_button = tkinter.Button(f7, text="View Data", command=view_menu, width=15)
    view_button.place(x=300, y=250)


    root7.mainloop()


def insert_menu():

    root2 = tkinter.Tk()
    root2.geometry('700x300')

    f2 = tkinter.Frame(root2, bg="#172c3e")
    f2.place(height=1000, width=1000)

    welcome_label = tkinter.Label(f2, text="Welcome to Art Gallery", font = 'Calibri 21' , fg='#FF5722',bg='#172c3e')
    welcome_label.place(x=100, y=50)

    choice_label = tkinter.Label(f2, text="Please select a department:",fg='yellow',bg='#172c3e')
    choice_label.place(x=100, y=100)

    artist_button = tkinter.Button(f2, text="Artist", command=artist_click)
    artist_button.place(x=100 , y=150)

    artwork_button = tkinter.Button(f2, text="Artwork", command=artwork_click)
    artwork_button.place(x=200, y=150)

    cust_button = tkinter.Button(f2, text="Customer", command=customer_click)
    cust_button.place(x=330, y=150)

    root2.mainloop()


def search_menu():

    root8 = tkinter.Tk()
    root8.geometry('700x300')

    f8 = tkinter.Frame(root8, bg="#172c3e")
    f8.place(height=1000, width=1000)

    welcome_label = tkinter.Label(f8, text="Welcome to Art Gallery", font = 'Calibri 21' , fg='#FF5722', bg='#172c3e')
    welcome_label.place(x=100, y=50)

    choice_label = tkinter.Label(f8, text="Please select a department:", fg='yellow', bg='#172c3e')
    choice_label.place(x=100, y=100)

    artist_sbutton = tkinter.Button(f8, text="Artist", command=artist_search)
    artist_sbutton.place(x=100, y=150)

    artwork_sbutton = tkinter.Button(f8, text="Artwork", command=artwork_search)
    artwork_sbutton.place(x=230, y=150)

    cust_sbutton = tkinter.Button(f8, text="Customer", command=customer_search)
    cust_sbutton.place(x=360, y=150)

    purchase_sbutton = tkinter.Button(f8, text="Purchase History", command=purchase_search, width=13)
    purchase_sbutton.place(x=490, y=150)

    root8.mainloop()


def artist_search():
    global root9, f9, artist_searchbox
    root9 = tkinter.Tk()
    root9.geometry('400x400')

    f9 = tkinter.Frame(root9, bg="#172c3e")
    f9.place(height=400, width=400)

    artist_slabel = tkinter.Label(f9, text="Enter Artist Name:", fg='yellow', bg='#172c3e')
    artist_slabel.place(x=100, y=50)

    artist_searchbox = tkinter.Entry(f9)
    artist_searchbox.place(x=100, y=100)

    submit = tkinter.Button(f9, text="Submit", command=artist_searchdata)
    submit.place(x=150, y=150)

    root9.mainloop()


def artwork_search():
    global root10, f10, artwork_searchbox
    root10 = tkinter.Tk()
    root10.geometry('400x400')

    f10 = tkinter.Frame(root10, bg="#172c3e")
    f10.place(height=400, width=400)

    artwork_slabel = tkinter.Label(f10, text="Enter Artwork Title:", fg='yellow', bg='#172c3e')
    artwork_slabel.place(x=100, y=50)

    artwork_searchbox = tkinter.Entry(f10)
    artwork_searchbox.place(x=100, y=100)

    submit = tkinter.Button(f10, text="Submit", command=artwork_searchdata)
    submit.place(x=150, y=150)

    root10.mainloop()

def customer_search():
    global root11, f11, customer_searchbox
    root11 = tkinter.Tk()
    root11.geometry('400x400')

    f11 = tkinter.Frame(root11, bg="#172c3e")
    f11.place(height=400, width=400)

    customer_slabel = tkinter.Label(f11, text="Enter Customer Name:", fg='yellow', bg='#172c3e')
    customer_slabel.place(x=100, y=50)

    customer_searchbox = tkinter.Entry(f11)
    customer_searchbox.place(x=100, y=100)

    submit = tkinter.Button(f11, text="Submit", command=customer_searchdata)
    submit.place(x=150, y=150)

    root11.mainloop()


def purchase_search():
    global root12, f12, purchase_searchbox
    root12 = tkinter.Tk()
    root12.geometry('800x800')

    f12 = tkinter.Frame(root12, bg="#172c3e")
    f12.place(height=800, width=800)

    purchase_slabel = tkinter.Label(f12, text="Enter Customer Name:", fg='yellow', bg='#172c3e')
    purchase_slabel.place(x=100, y=50)

    purchase_searchbox = tkinter.Entry(f12)
    purchase_searchbox.place(x=100, y=100)

    submit = tkinter.Button(f12, text="Submit", command=purchase_searchdata)
    submit.place(x=150, y=150)

    root12.mainloop()

def delete_menu():

    root13 = tkinter.Tk()
    root13.geometry('700x300')

    f13 = tkinter.Frame(root13, bg="#172c3e")
    f13.place(height=1000, width=1000)

    welcome_label = tkinter.Label(f13, text="Welcome to Art Gallery", font = 'Calibri 21' , fg='#FF5722', bg='#172c3e')
    welcome_label.place(x=100, y=50)

    choice_label = tkinter.Label(f13, text="Please select a department to delete records from:", fg='yellow', bg='#172c3e')
    choice_label.place(x=100, y=100)

    artist_dbutton = tkinter.Button(f13, text="Artist", command=artist_delete)
    artist_dbutton.place(x=100, y=150)

    artwork_dbutton = tkinter.Button(f13, text="Artwork", command=artwork_delete)
    artwork_dbutton.place(x=200, y=150)

    cust_dbutton = tkinter.Button(f13, text="Customer", command=customer_delete)
    cust_dbutton.place(x=330, y=150)

    root13.mainloop()


def artist_delete():
    global root14, f14, artist_deletebox
    root14 = tkinter.Tk()
    root14.geometry('400x400')

    f14 = tkinter.Frame(root14, bg="#172c3e")
    f14.place(height=400, width=400)

    artist_slabel = tkinter.Label(f14, text="Enter Artist Name to delete:", fg='yellow', bg='#172c3e')
    artist_slabel.place(x=100, y=50)

    artist_deletebox = tkinter.Entry(f14)
    artist_deletebox.place(x=100, y=100)

    submit = tkinter.Button(f14, text="Submit", command=artist_del)
    submit.place(x=153, y=150)

    root14.mainloop()


def artwork_delete():
    global root15, f15, artwork_deletebox
    root15 = tkinter.Tk()
    root15.geometry('400x400')

    f15 = tkinter.Frame(root15, bg="#172c3e")
    f15.place(height=400, width=400)

    artwork_slabel = tkinter.Label(f15, text="Enter Artwork Title to delete:", fg='yellow', bg='#172c3e')
    artwork_slabel.place(x=100, y=50)

    artwork_deletebox = tkinter.Entry(f15)
    artwork_deletebox.place(x=100, y=100)

    submit = tkinter.Button(f15, text="Submit", command=artwork_del)
    submit.place(x=150, y=150)

    root15.mainloop()

def customer_delete():
    global root16, f16, customer_deletebox
    root16 = tkinter.Tk()
    root16.geometry('400x400')

    f16 = tkinter.Frame(root16, bg="#172c3e")
    f16.place(height=400, width=400)

    customer_slabel = tkinter.Label(f16, text="Enter Customer Name to delete:", fg='yellow', bg='#172c3e')
    customer_slabel.place(x=100, y=50)

    customer_deletebox = tkinter.Entry(f16)
    customer_deletebox.place(x=100, y=100)

    submit = tkinter.Button(f16, text="Submit", command=customer_del)
    submit.place(x=150, y=150)

    root16.mainloop()


def update_menu():

    root18 = tkinter.Tk()
    root18.geometry('500x400')

    f18 = tkinter.Frame(root18, bg="#172c3e")
    f18.place(height=1000, width=1000)

    welcome_label = tkinter.Label(f18, text="Welcome to Art Gallery", font = 'Calibri 21' , fg='#FF5722', bg='#172c3e')
    welcome_label.place(x=100, y=50)

    choice_label = tkinter.Label(f18, text="Please select a department to update records from:", fg='yellow', bg='#172c3e')
    choice_label.place(x=100, y=100)

    artist_ubutton = tkinter.Button(f18, text="Artist", command=artist_update)
    artist_ubutton.place(x=100, y=150)

    artwork_ubutton = tkinter.Button(f18, text="Artwork", command=artwork_update)
    artwork_ubutton.place(x=200, y=150)

    cust_ubutton = tkinter.Button(f18, text="Customer", command=customer_update)
    cust_ubutton.place(x=330, y=150)

    root18.mainloop()


def artist_update():
    global root19, f19, artist_updatebox
    root19 = tkinter.Tk()
    root19.geometry('500x500')

    f19 = tkinter.Frame(root19, bg="#172c3e")
    f19.place(height=500, width=900)

    artist_slabel = tkinter.Label(f19, text="Enter Artist Name to update:", fg='yellow', bg='#172c3e')
    artist_slabel.place(x=100, y=50)

    artist_updatebox = tkinter.Entry(f19)
    artist_updatebox.place(x=100, y=100)

    submit = tkinter.Button(f19, text="Submit", command=artist_up)
    submit.place(x=150, y=150)

    root19.mainloop()


def artwork_update():
    global root20, f20, artwork_updatebox
    root20 = tkinter.Tk()
    root20.geometry('500x550')

    f20 = tkinter.Frame(root20, bg="#172c3e")
    f20.place(height=550, width=900)

    artwork_slabel = tkinter.Label(f20, text="Enter Artwork Title to update:", fg='yellow', bg='#172c3e')
    artwork_slabel.place(x=100, y=50)

    artwork_updatebox = tkinter.Entry(f20)
    artwork_updatebox.place(x=100, y=100)

    submit = tkinter.Button(f20, text="Submit", command=artwork_up)
    submit.place(x=150, y=150)

    root20.mainloop()

def customer_update():
    global root21, f21, customer_updatebox
    root21 = tkinter.Tk()
    root21.geometry('500x500')

    f21 = tkinter.Frame(root21, bg="#172c3e")
    f21.place(height=500, width=900)

    customer_slabel = tkinter.Label(f21, text="Enter Customer Name to update:", fg='yellow', bg='#172c3e')
    customer_slabel.place(x=100, y=50)

    customer_updatebox = tkinter.Entry(f21)
    customer_updatebox.place(x=100, y=100)

    submit = tkinter.Button(f21, text="Submit", command=customer_up)
    submit.place(x=150, y=150)

    root21.mainloop()


def purchase_update():
    global root22, f22, purchase_updatebox
    root22 = tkinter.Tk()
    root22.geometry('500x500')

    f22 = tkinter.Frame(root22, bg="#172c3e")
    f22.place(height=500, width=500)

    purchase_slabel = tkinter.Label(f22, text="Enter Artwork Title to update:", fg='yellow', bg='#172c3e')
    purchase_slabel.place(x=100, y=50)

    purchase_updatebox = tkinter.Entry(f22)
    purchase_updatebox.place(x=100, y=100)

    submit = tkinter.Button(f22, text="Submit", command=func1)
    submit.place(x=150, y=150)

    root22.mainloop()


def login_submit():

    uname = uname_textbox.get()
    pw = pw_textbox.get()
    if (uname == 'admin' and pw == 'pw'):
        main_menu()
    else:
        error = tkinter.Label(f1, text="Wrong ID / Password",fg='yellow',bg='#172c3e')
        error.place(x=170 , y=250)


def login_menu():
    global f1, uname_textbox, pw_textbox

    root = tkinter.Tk()
    root.geometry('450x300')

    f1 = tkinter.Frame(root, bg = "#172c3e")
    f1.place(height=500, width=500)

    welcome_label = tkinter.Label(f1, text="Login Page",fg='yellow',bg='#172c3e')
    welcome_label.place(x=190, y=50)

    uname_label = tkinter.Label(f1, text="Username:",fg='yellow',bg='#172c3e')
    uname_label.place(x=50, y=100)

    uname_textbox = tkinter.Entry(f1)
    uname_textbox.place(x=150, y=100)

    pw_label = tkinter.Label(f1, text="Password:",fg='yellow',bg='#172c3e')
    pw_label.place(x=50, y=150)

    pw_textbox = tkinter.Entry(f1, show="*")
    pw_textbox.place(x=150, y=150)

    sub = tkinter.Button(f1, text="Submit", command = login_submit, bg='#172c3e')
    sub.place(x=200, y=200)

    root.mainloop()

login_menu()