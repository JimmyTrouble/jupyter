#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qiskit


# In[2]:


import numpy as np


# In[4]:


from qiskit import QuantumCircuit , QuantumRegister , ClassicalRegister , execute , IBMQ


# In[6]:


from qiskit.tools.visualization import circuit_drawer


# In[3]:


from qiskit import QuantumCircuit , QuantumRegister , ClassicalRegister , execute , IBMQ


# In[4]:


qc = QuantumCircuit(1)
qc.draw('mpl') 


# In[6]:


qc = QuantumCircuit(1)
qc.draw('mpl') 


# In[11]:


from qiskit.tools.visualization import circuit_drawer
circuit_drawer(qc, output= 'text')

