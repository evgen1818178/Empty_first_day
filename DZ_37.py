import sqlite3

stream = sqlite3.connect("database_37.db")
cur = stream.cursor()

try:
    NewTable = """CREATE TABLE Participants(ID INTEGER, Surname TEXT, Name TEXT, Patronymic TEXT, Academic_degree TEXT, Scientific_direction TEXT, Workplace TEXT, Cathedra TEXT, Post TEXT, County TEXT, City TEXT, Address TEXT, Work_phone TEXT, Email TEXT);"""
    cur.execute(NewTable)
    NewTable = """CREATE TABLE Activities(ID INTEGER, Speaker TEXT, date_of_invitation TEXT, date_of_receipt TEXT, topic_of_the_report TEXT, receipt_of_abstracts TEXT, arrival_date TEXT, need_for_a_hotel TEXT, departure_date TEXT);"""
    cur.execute(NewTable)
    NewTable = """CREATE TABLE Conferences(ID INTEGER, Сonference_name TEXT, date_of_event TEXT, Place TEXT, Organizers_ID TEXT, Sponsors_ID TEXT, Event_length TEXT, number_of_participants TEXT, number_of_speakers TEXT);"""
    cur.execute(NewTable)
except:
    pass

stream.commit()
cur.close()
stream.close()