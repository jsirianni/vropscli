# Basic Usage

First, make sure you have a .vropscli.yml file in your home directory.  It's format should be as
```
default:
    host: "vrops.domain.tld"
    user: "admin"
    pass: "password"

```
Test by running ```vropscli getAdapters``` and verify you are getting current information back

# Install/Upgrade Management Packs

First, you will need to uplaod the management pack...this may take some time
```
vropscli uploadPak OracleDatabase-6.3_1.2.0_b20180319.144115.pak
```
Once the upload is done, you will be provided with a pak_id.  Use that to start to install/upgrade.
```
vropscli installPak OracleDatabase-12020180319144115
```
You can track the current progress wtih
```
vropscli getCurrentActivity
```

# Install Licensing

First determine the id of the solution that was installed as part of the Management pack

```
vropscli getSolution solution
```

Use the "id" from above for the correct management pack to install the license

```
vropscli setSolutionLicense OracleDatabase 4/trialparticipant/06-20-2018-17:30:18/BM-VREALIZE-ORACLE-DB/trial/06-22-2018-17:30:18/MP/accumulating/BM-VREALIZE-ORACLE-DB/Unlimited/C4B2F9E09CF0BADB867F1DAAF32AEAC6DDAF6473
```

Get current lienses installed

```
vropscli getSolutionLicense OracleDatabase
```

# Stop/start Adapter Instances

Lookup Adapter Instance UUIDs

```
vropscli getAdapters
```

Stop Adapter Instance

```
vropscli stopAdapterInstance 9516b17d-f2a5-4da0-ab12-c4998dc0889e
```

Start Adapter Instance

```
vropscli startAdapterInstance 9516b17d-f2a5-4da0-ab12-c4998dc0889e
```

# Setup new adapter instances

First, setup one instance of the adapter will all settings and credentials.  Once you have confirmed that works

## Determein the specific adapter and the AdapterKind from the example you created 
```
vropscli getAdapters
```
The Name is the second fieldd.  Record the following info for the adapter you just created
* UUID (first field)
* AdapterKind (3rd field)

## Generate an example CSV file based on the example you created, using hte AdapterKind for step 1

```
vropscli getAdapterConfig  62cae133-2233-4880-9136-a07e2f00ecfa > newadapter.csv
```

## Get the UUID of the credential you are planning to use with your other instances

```
vropscli getCredentials 
```

## Adjust the CSV file to include all the new instances based on the exampel you created.  The inital "exmaple" should be
removed from the csv.  Once complete, create the new instances

```
vropscli createAdapterInstances <AdapterKind> <CSVfile> <UUID of credential> 
```
Example:
```
vropscli createAdapterInstances NAGIOS_ADAPTER adapter.csv 2de121e4-9550-443f-93a0-181865d01045
```