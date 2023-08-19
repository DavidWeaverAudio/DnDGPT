# DnDGPT
A helper tool for DM's to be able to generate NPCs for one shots or campaign items with some fun backstory, personality and lore.

If you've got a BUNCH of training data, you can type out your prompts to get fun descriptions of fakelore for your homebrew campaign or one shot!
![image](https://github.com/DavidWeaverAudio/DnDGPT/assets/78392269/ef8ff223-9a07-42f9-8de8-840d39ee4cd5)

Simple go to openAI and set up an API key : https://platform.openai.com/docs/api-reference

Then add the API key to the places indicated in;
- app.py
- create_model.sh

Then run the batch commands with your jsonl file
FOR EXAMPLE 
./fine_tune.sh training_data_prepared.jsonl
./create_model.sh training_data_prepared.jsonl

Then, once the model has been prepared, copy the model into the app.py script, replacing model= spot to start generating!
Run app.py, open the localhost and click the generate button!

And hey, if you want to write another few thousand elements for the training data to actually make it useful, go nuts!
