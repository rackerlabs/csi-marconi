Test Definitions
-----------------

**Scenario** - Is a group of Test Cases.  Each user will execute all the Test Cases in a scenario (in the sequence defined in the scenario). The load test will have multiple Scenarios, all which will run in parallel. Each scenario has a given probability. This is used to decide which session a new user will execute.

Example - Assuming load test defines 1000 new users/second,
At any given second, we'll have
  #. 100 Users running Scenario 1 (each of them executing tests 1 thru 5 in sequence)
  #. 100 Users running Scenario 2 (each of them executing tests 1 thru 6 in sequence)
  #. 100 Users running Scenario 3
  #. 100 Users running Scenario 4
  #. 600 Users running Scenario 5

**Test Definitions (defined in tsung.xml)**

  Scenario-1 : Probability 10
    #. Create Queue with random name
    #. Post Message to the queue
    #. Get Message
    #. Get Queue Stats
    #. Delete Queue

  Scenario-2 : Probability 10
    #. Create Queue with random name
    #. Post Message to the queue
    #. Get Queue metadata
    #. Update Queue metadata
    #. Delete Queue
    #. Get Queue

  Scenario-3 : Probability 10
    #. Create Queue with random name
    #. Post Message to the queue
    #. Claim message
    #. Update Claim from Step 
    #. Delete Claimed messages
    #. Claim message
    #. Get Queue Stats
    #. Delete Queue

  Scenario-4 : Probability 10
    #. Create Queue with random name
    #. Post Message to the queue 
    #. Claim message
    #. Delete Claimed messages
    #. List Queues
    #. Delete Queue

  Scenario-5 : Probability 60 (See NOTE 1)
    #. Post 10 Messages to an existing queue - Loop 500 times
    #. Get Messages
    #. Claim messages with limit=5
    #. Delete Claimed messages
    #. Claim messages with limit=8
    #. Delete Claimed messages
    #. Claim messages with limit=1
    #. Delete Claimed messages
    #. Delete Claim

  NOTE 1 : We expect a lot more post messages & claim, than create/list queues . Hence this has a higher probability
