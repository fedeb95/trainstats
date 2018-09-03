# Trainstats

Software for gathering data about trenord's delays.

Data is collected from http://mobile.my-link.it/mylink/mobile/stazione

# Usage

Clone this repository and schedule `/path/to/python3 /path/to/trainstats/runner.py /path/to/config` to run every n minutes, as desired. You can set your crontab at 4, for instance.
`runner.py` can be modified to include every station you can search with the website at top. In the future this should be
specified in the configuration file.

For the program to work you need a configuration file with:
```
{
  "conn_string":"mongodb:<user>:<password>@<address>:<port>/<database_name>"
}
```

# Data visualisation
In `utils` module there are some functions to visualise data with matplotlib or pandas. Feel free to contribute with your graphs too.

# To be done
Stations will be in the configuration file. Also the database columns, used everywhere and now in italian, should be specified there,
in english.

I plan to also provide a website with some stats 
