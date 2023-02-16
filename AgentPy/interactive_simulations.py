#!/usr/bin/env python
# coding: utf-8

# In[1]:


import agentpy as ap
import ipysimulate as ips

from ipywidgets import AppLayout
from agentpy.examples import WealthModel, SegregationModel


# In[2]:


model = WealthModel()


# In[3]:


parameters = {
    "agents": 1_000,
    "steps": 100,
    "fps": ap.IntRange(1, 20, 5),
}


# In[4]:


# Display time-steps and gini parameters live during the simulation
control = ips.Control(
    model,
    parameters,
    variables=("t", "gini")
)


# In[5]:


# Create line plot of gini variable
lineplot = ips.Lineplot(control, "gini")


# In[6]:


# Create layout to display control and lineplot
AppLayout(
    left_sidebar=control,
    center=lineplot,
    pane_widths=["125px", 1, 1],
    height="400px",
)


# In[ ]:




