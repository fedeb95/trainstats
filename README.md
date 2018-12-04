# Trainstats

Software for gathering data about trenord's delays.

Data is collected from http://mobile.my-link.it/mylink/mobile/stazione

# Usage

Clone this repository and run `/path/to/python3 /path/to/trainstats/runner.py /path/to/config`. You can also use the provided Dockerfile.

For the program to work you need a configuration file like this:
```
{
  "conn_string":"mongodb://<user>:<password>@<address>:<port>/<database_name>",
  "timer":"240",
  "stations":["brescia","milano centrale"]
}
```
You can specify whichever station or update time in seconds you like, as you would search it on trenord's website.

# Data visualisation
In `utils` module there are some functions to visualise data with matplotlib or pandas. Feel free to contribute.

# To be done
Database columns, used everywhere and now in italian, should be specified in the configuration file. A procedure to also convert existing columns to new ones should be provided.
