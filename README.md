Create a file in dungeonMaster/settings/ <your filename>.py and put your server settings in there.
If you need reference you can see george.py

After you have setted up the settings file
  -Database
  -Template dir
  -Static dir
  
Crete the tables in the database by running

python manage.py syncdb --settings=dungeonMaster.settings.<your filename>.py

after sync is done populate by

python manage.py shell --settings=dungeonMaster.settings.<your filename>.py

and running

execfile('sampleData.py')

after the population was successful run the server

python manage.py runserver --settings=dungeonMaster.settings.<your filename>.py

================================================================

Link to repo:
https://github.com/MrJew/dungeonMaster

No other external packages are needed
