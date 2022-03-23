
qch = Venue(name="Queen City Hemp", street_address="6 Kovach Dr #620",
city="Cincinnati", state="OH", zip="45215")
db.session.add(qch)

ct = Artist(name="The Cliftones")
db.session.add(ct)

db.session.commit()

tix_link = "www.eventbrite.com/e/277709646027"
abt = """It's the return of The Cliftones!
After over, TWO YEARS, the Cliftones will return to the stage live at Queen City Hemp's Jam in the Can!
Queen City Hemp & Animal Discourse are happy to present the return of the Cliftones in concert, after a two year hiatus, live at Queen City Hemp. This event will also feature DJ sets from MetaModernMusic before and after The Cliftones headlining set, complimentary Queen City Hemp Seltzers, and a food truck. This will be an intimate event with limited tickets, so we can present you with a truly original experience."""

from datetime import datetime
door = datetime(2022, 3, 26, 19, 00, 00)
end = datetime(2022, 3, 26, 23, 00, 00)
ct_3_26 = Event(title="The Cliftones!", event_door=door,
event_end=end, artist=ct, venue=qch, price=20,
ticket_link=tix_link, ages="18+", about=abt)

db.session.add(ct_3_26)
db.session.commit()
