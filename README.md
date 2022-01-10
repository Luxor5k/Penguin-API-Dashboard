# Penguins (Mid-Project BDMLPT1021) 🐧

<p align="center"> 
  The function of this api is to study penguins that live in "Palmer Archipelago" like this: 
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/62902607/147587683-5aa4aae9-052a-49b7-9474-acf67bd3bdcb.jpg" width="400">
</p>

<p align="center">
  You can search different penguins by their ID, getting your statistics / name / island and other data. Also has the possibility to show graphics with some data of penguins of the islands
</p>

## Getting Started

### Requirements:

- [API](https://github.com/Luxor5k/mid_project/blob/main/api/requirements.txt)
- [DASHBOARD](https://github.com/Luxor5k/mid_project/blob/main/dashboard/requirements.txt)


Uvicorn run:
```sh
  uvicorn api.main:app 
  ```
  This command is to run the API in our computer

Streamlit run:
```sh
  streamlit run main.py
  ```
  This command is to run the dashboard in our computer 
  
 ## Roadmap
 
 - [x] Obtain data about a penguin by their ID (Name, stats, island)
 - [x] Show differents average stats
 - [ ] Compare
     - [ ] A penguin to another
     - [ ] A penguin to average data
 - [ ] Show the location of islands in a map
 - [ ] Add data through the page
  
