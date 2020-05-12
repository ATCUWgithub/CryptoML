# Infrastructure

EXAMPLE USECASE

```python
import crypto_ml

# Load the data from 12/23/2019 - 12/30/2019
data_json = crypto_ml.utils.load_json("./test_data/subset_data.json")

# Generate config from smallest dataset
config = crypto_ml.utils.generate_config(data_json)

# Load Data, Agent, Wallet
data_raw = crypto_ml.DataRaw(crypto_ml.OrderType.CONTINOUS, data_json)
agent = crypto_ml.agent.SimpleAgent([data_raw])
wallet = crypto_ml.Wallet(1.0) 

# Create Simulator
simulator = crypto_ml.Simulator(wallet, agent, config)

# Run Simulator for all timesteps
simulator.run()

# To get the ROI of the algorithim  
simulator.roi()
```

