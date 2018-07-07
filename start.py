from NoteMakingDB import NoteMakingDB
from dashboard import Dashboard

#try:
# Add Your Database username and password here
db = NoteMakingDB(username="badoni97", password="shiavnibadoni@gmail.com")
Dashboard().initUI(db)

#except Exception as e:
#   messagebox.showinfo("Error", "Unable to establish database connection.")
