# digiato
A crawler that contains news from digiato website.

## How To Use

* install the requirements

* in ```models.py``` import the name below


  ```from playhouse.db_url import connect```

* create your database connect to your database like the example below

  ```database = connect('mysql://USERNAME:PASSWORD@127.0.0.1:3306/digiato')```

* run ``` $ main.py find_and_store_links ```

* run ``` $ main.py read_links```

# 
Now you got all your news in seprated categories in your database:)
