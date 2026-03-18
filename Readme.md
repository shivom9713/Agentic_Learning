## Env creation


To create virtual ENV
```
python -m venv 'myenv'
```

```
cd 'envlocation'
./Scripts/activate
```

```
pip install langgraph
pip install langchain
pip install langchain_openai
pip install langchain-openai
pip install dotenv
pip install streamlit

pip install langgraph-checkpoint-sqlite 
```

## To visualize workflows
```
pip install ipython
pip install grandalf
```


### To Persist

We can use the In - Memory Saver and using threads for tracking conversations
However the downside is that, as soon as the app data is removed from RAM or memory, you can't track it back.

To resolve this we use SQLITE Integration with Langchain for storing checkpoints.
