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
pip install -U langchain-tavily ## for internet search
```

## To visualize workflows
```
pip install ipython
pip install grandalf
```

#### For Jupyter testing 

```
pip install ipykernel jupyter
```

### Internet Search related tools

```
pip install -qU duckduckgo-search langchain-community
pip install -U ddgs
```


### To Persist

We can use the In - Memory Saver and using threads for tracking conversations
However the downside is that, as soon as the app data is removed from RAM or memory, you can't track it back.

To resolve this we use SQLITE Integration with Langchain for storing checkpoints.


### Defining Structured output with Pydantic 

We use `Pydantic` which inherits from the Base class to define the expected output in an structured format. Once we generate the structured output we use this response format to update the Langgraph State from the Node

### Defining the State:

State can be defined using `TypedDict` class for structuring the intended format
