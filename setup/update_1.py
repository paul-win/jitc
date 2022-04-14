#FILE SYSTEM setup:

#add JitC-Pop-Tab-icon.png file to static/media/ folder
#add cover.jpg file to static/media/cliftones_3_26_2022/ folder
#add cover.jpg to static/media/qch/ folder (create folder)
#create calumet media folder static/media/calumet_9_3_2021/
#copy tracks into folder
#create almost infinite folder static/media/the_almost_infinite_8_6_2021
#copy tracks into folder
#create slow glows folder static/media/slow_glows_3_4_2022
#copy tracks into folder
#create dead humor folder static/media/dead_humor_7_9_2021
#copy tracks into folder
#create EJFD folder static/media/ejfd_12_4_2021
#copy tracks into folder

#MYSQL setup:

#add media_dir column to venue table
    ## mysql> use jitc;
    ## mysql > alter table venue add column media_dir varchar(128) after zip;
#modify db for length field in jams table
    ## mysql> use jitc;
    ## mysql> alter table jam add column length TIME after title;


#PYTHON setup:

#add media_dir path to qch venue record
qch = Venue.query.get(1)
#ensure == qch
qch.media_dir = 'media/qch/'
db.session.add(qch)
db.session.commit()

#remove static/ from media_dir for cliftones events
e = Event.query.get(1)
#ensure e = cliftones
e.media_dir = e.media_dir.replace('static/', '')
db.session.add(e)
db.session.commit()

#add Calumet
cal = Artist(name="Calumet")
db.session.add(cal)
db.session.commit()

#add calumet event
from datetime import datetime
door = datetime(2021, 9, 3)
calumet = Event(title="Calumet", event_door=door,
artist=cal, venue=qch)
calumet.media_dir = 'media/calumet_9_3_2021/'
db.session.add(calumet)
db.session.commit()

#create jams
j1 = Jam(event=calumet, artist=cal, track_num=1, title='Somewhere', length='00:03:48', file='somewhere.mp3')
j2 = Jam(event=calumet, artist=cal, track_num=2, title='Straight to the Bottom', length='00:04:42', file='straight_to_the_bottom.mp3')
j3 = Jam(event=calumet, artist=cal, track_num=3, title='This is Wrong', length='00:05:00', file='this_is_wrong.mp3')
j4 = Jam(event=calumet, artist=cal, track_num=4, title='Lil Bit', length='00:03:32', file='lil_bit.mp3')
j5 = Jam(event=calumet, artist=cal, track_num=5, title='Open Fire', length='00:04:31', file='open_fire.mp3')
j6 = Jam(event=calumet, artist=cal, track_num=6, title='Selling Fiction', length='00:03:58', file='selling_fiction.mp3')
j7 = Jam(event=calumet, artist=cal, track_num=7, title='Indian Summer', length='00:03:58', file='indian_summer.mp3')
j8 = Jam(event=calumet, artist=cal, track_num=8, title='Closer to You', length='00:03:54', file='closer_to_you.mp3')
j9 = Jam(event=calumet, artist=cal, track_num=9, title='Waited a Long Time', length='00:03:24', file='waited_a_long_time.mp3')
j10 = Jam(event=calumet, artist=cal, track_num=10, title='Rough & Ready', length='00:04:17', file='rough_and_ready.mp3')
j11 = Jam(event=calumet, artist=cal, track_num=11, title='Reconcile', length='00:06:34', file='reconcile.mp3')
j12 = Jam(event=calumet, artist=cal, track_num=12, title='Go My Way', length='00:03:40', file='go_my_way.mp3')
j13 = Jam(event=calumet, artist=cal, track_num=13, title='Barnburner', length='00:05:17', file='barnburner.mp3')
j14 = Jam(event=calumet, artist=cal, track_num=14, title='Change', length='00:03:12', file='change.mp3')
j15 = Jam(event=calumet, artist=cal, track_num=15, title='Idaho', length='00:05:22', file='idaho.mp3')

db.session.add_all([j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15])
db.session.commit()

#almost infinite set up
tai = Artist(name="The Almost Infinite")
db.session.add(tai)
db.session.commit()

door = datetime(2021, 8, 6)
tai_e = Event(title="The Almost Infinite", event_door=door, artist=tai, venue=qch)
tai_e.media_dir = 'media/the_almost_infinite_8_6_2021/'
db.session.add(tai_e)
db.session.commit()

j1 = Jam(event=tai_e, artist=tai, track_num=1, title='Nameless', length='00:02:09', file='Nameless.mp3')
j2 = Jam(event=tai_e, artist=tai, track_num=2, title='See You in Hell', length='00:03:33', file='See_You_in_Hell.mp3')
j3 = Jam(event=tai_e, artist=tai, track_num=3, title='Get Out', length='00:04:49', file='Get_Out.mp3')
j4 = Jam(event=tai_e, artist=tai, track_num=4, title='Family History', length='00:05:34', file='Family_History.mp3')
j5 = Jam(event=tai_e, artist=tai, track_num=5, title='Long Brown Hair', length='00:02:25', file='Long_Brown_Hair.mp3')
j6 = Jam(event=tai_e, artist=tai, track_num=6, title='Tried So Hard', length='00:05:04', file='Tried_So_Hard.mp3')
j7 = Jam(event=tai_e, artist=tai, track_num=7, title='Monster', length='00:05:01', file='Monster.mp3')

db.session.add_all([j1,j2,j3,j4,j5,j6,j7])
db.session.commit()

#slow glows setup
sg = Artist(name="Slow Glows")
db.session.add(sg)
db.session.commit()

door = datetime(2022, 3, 4)
sg_e = Event(title="Slow Glows", event_door=door, artist=sg, venue=qch)
sg_e.media_dir = 'media/slow_glows_3_4_2022/'
db.session.add(sg_e)
db.session.commit()

j1 = Jam(event=sg_e, artist=sg, track_num=1, title='Introduction/Jam in the Can Update', length='00:02:51', file='Introduction_Jam_in_the_Can_Update.mp3')
j2 = Jam(event=sg_e, artist=sg, track_num=2, title='December', length='00:04:57', file='December.mp3')
j3 = Jam(event=sg_e, artist=sg, track_num=3, title='Spiderland', length='00:04:33', file='Spiderland.mp3')
j4 = Jam(event=sg_e, artist=sg, track_num=4, title='Geode', length='00:05:47', file='Geode.mp3')
j5 = Jam(event=sg_e, artist=sg, track_num=5, title='Daydreamer', length='00:04:00', file='Daydreamer.mp3')
j6 = Jam(event=sg_e, artist=sg, track_num=6, title='Sigh', length='00:05:14', file='Sigh.mp3')
j7 = Jam(event=sg_e, artist=sg, track_num=7, title='Mosaic', length='00:06:09', file='Mosaic.mp3')
j8 = Jam(event=sg_e, artist=sg, track_num=8, title='The End', length='00:08:35', file='The_End.mp3')
j9 = Jam(event=sg_e, artist=sg, track_num=9, title='Cast a Shadow', length='00:05:34', file='Cast_a_Shadow.mp3')


db.session.add_all([j1,j2,j3,j4,j5,j6,j7,j8,j9])
db.session.commit()


#dead humor setup
dh = Artist(name="Dead Humor")
db.session.add(dh)
db.session.commit()

door = datetime(2021, 7, 9)
dh_e = Event(title="Dead Humor", event_door=door, artist=dh, venue=qch)
dh_e.media_dir = 'media/dead_humor_7_9_2021/'
db.session.add(dh_e)
db.session.commit()

j1 = Jam(event=dh_e, artist=dh, track_num=1, title="Jam Medley", length="00:22:40", file="Jam_Medley.mp3")


db.session.add(j1)
db.session.commit()


#EJFD setup
ejfd = Artist(name="Ernie Johnson From Detroit")
db.session.add(ejfd)
db.session.commit()

door = datetime(2021, 12, 4)
ejfd_e = Event(title="Ernie Johnson From Detroit", event_door=door, artist=ejfd, venue=qch)
ejfd_e.media_dir = 'media/ejfd_12_4_2021/'
db.session.add(dh_e)
db.session.commit()

j1 = Jam(event=ejfd_e, artist=ejfd, track_num=1, title='Tony Allen Pro Skater II', length='00:09:27', file='Tony_Allen_Pro_Skater_II.mp3')
j2 = Jam(event=ejfd_e, artist=ejfd, track_num=2, title='Skylode', length='00:07:47', file='Skylode.mp3')
j3 = Jam(event=ejfd_e, artist=ejfd, track_num=3, title='Heaven', length='00:08:07', file='Heaven.mp3')
j4 = Jam(event=ejfd_e, artist=ejfd, track_num=4, title='12 Fish', length='00:09:03', file='12_Fish.mp3')
j5 = Jam(event=ejfd_e, artist=ejfd, track_num=5, title='Give It Up (The Crusaders)', length='00:05:20', file='Give_It_Up.mp3')
j6 = Jam(event=ejfd_e, artist=ejfd, track_num=6, title='Red Foxxx', length='00:07:33', file='Red_Foxxx.mp3')
j7 = Jam(event=ejfd_e, artist=ejfd, track_num=7, title="Walt's First Trip (Ohio Players)", length='00:06:17', file='Walts_First_Trip.mp3')
j8 = Jam(event=ejfd_e, artist=ejfd, track_num=8, title='Murrgenta', length='00:07:28', file='Murrgenta.mp3')
j9 = Jam(event=ejfd_e, artist=ejfd, track_num=9, title='African Pop Session (Manu Dibango)', length='00:06:06', file='African_Pop_Session.mp3')
j10 = Jam(event=ejfd_e, artist=ejfd, track_num=10, title='Roy Tailors Uniform Co.', length='00:07:11', file='Roy_Tailors_Uniform_Co.mp3')
j11 = Jam(event=ejfd_e, artist=ejfd, track_num=11, title='Tiddy Bounce', length='00:10:24', file='Tiddy_Bounce.mp3')
j12 = Jam(event=ejfd_e, artist=ejfd, track_num=12, title="Ram's Horn", length='00:08:13', file='Rams_Horn.mp3')
j13 = Jam(event=ejfd_e, artist=ejfd, track_num=13, title='Unicorn (Dizzy Gillespie)', length='00:06:08', file='Unicorn.mp3')

db.session.add_all([j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13])
db.session.commit()