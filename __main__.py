import sys, os

from game import Game
from human_player import Human

from AI.simple_player import SimpleAgent
from  AI.random_player import randomAgent
from  AI.probability_player import ProbAgent
from  AI.simple_player_memory import ModelAgent
from AI.Learning_player import LearningAgent
if len(sys.argv) < 2:
    print("Error: Usage is __main__.py 'number of games' ")
    exit(1)
if len(sys.argv) == 3:
    if sys.argv[2] == "-np":
        sys.stdout = open(os.devnull, 'w')

AgentWins = 0
AgentLosses = 0
AgentTies = 0
i = 0
#player_name = input("What is you name: ")
while i < int(sys.argv[1]):
    players = [ModelAgent(brisChance = 0.1 , chance = 0.35, name = "Simple"), LearningAgent(name = "Model",brisChance=0,chance=
                                                                                            {'pointless': {1.0: 0.64, 0.99: 0.98, 0.98: 0.35, 0.97: 0.48, 0.96: 0.98, 0.95: 0.92, 0.94: 0.28, 0.93: 0.83, 0.92: 0.1, 0.91: 0.5, 0.9: 0.66, 0.89: 0.45, 0.88: 0.98, 0.87: 0.23, 0.86: 0.72, 0.85: 0.72, 0.84: 0.11, 0.83: 0.24, 0.82: 0.22, 0.81: 0.02, 0.8: 0.97, 0.79: 0.18, 0.78: 0.52, 0.77: 0.67, 0.76: 0.07, 0.75: 0.95, 0.74: 0.96, 0.73: 0.88, 0.72: 0.63, 0.71: 0.9, 0.7: 0.25, 0.69: 0.32, 0.68: 0.2, 0.67: 0.1, 0.66: 0.33, 0.65: 0.08, 0.64: 0.15, 0.63: 0.68, 0.62: 0.57, 0.61: 0.95, 0.6: 0.44, 0.59: 0.08, 0.58: 0.75, 0.57: 0.82, 0.56: 0.73, 0.55: 0.18, 0.54: 0.01, 0.53: 0.06, 0.52: 0.83, 0.51: 0.92, 0.5: 0.17, 0.49: 0.07, 0.48: 0.26, 0.47: 0.48, 0.46: 0.7, 0.45: 0.69, 0.44: 0.95, 0.43: 0.31, 0.42: 0.64, 0.41: 0.84, 0.4: 0.92, 0.39: 0.59, 0.38: 0.38, 0.37: 0.68, 0.36: 0.44, 0.35: 0.58, 0.34: 0.33, 0.33: 0.6, 0.32: 0.94, 0.31: 0.19, 0.3: 0.74, 0.29: 0.4, 0.28: 0.67, 0.27: 0.16, 0.26: 0.25, 0.25: 0.63, 0.24: 0.79, 0.23: 0.52, 0.22: 0.44, 0.21: 0.06, 0.2: 0.95, 0.19: 0.88, 0.18: 0.65, 0.17: 0.58, 0.16: 0.13, 0.15: 0.31, 0.14: 0.3, 0.13: 0.58, 0.12: 0.19, 0.11: 0.51, 0.1: 0.02, 0.09: 0.76, 0.08: 0.22, 0.07: 0.44, 0.06: 0.44, 0.05: 0.63, 0.04: 0.32, 0.03: 0.91, 0.02: 0.67, 0.01: 0.55, 0.0: 0.29}, 'brispointless': {1.0: 0.84, 0.99: 0.97, 0.98: 0.95, 0.97: 0.38, 0.96: 0.18, 0.95: 0.46, 0.94: 0.45, 0.93: 0.47, 0.92: 0.66, 0.91: 0.82, 0.9: 0.45, 0.89: 0.96, 0.88: 0.51, 0.87: 0.59, 0.86: 0.91, 0.85: 0.83, 0.84: 0.12, 0.83: 0.91, 0.82: 0.62, 0.81: 0.41, 0.8: 0.79, 0.79: 0.29, 0.78: 0.57, 0.77: 0.37, 0.76: 0.48, 0.75: 0.14, 0.74: 0.58, 0.73: 0.43, 0.72: 0.28, 0.71: 0.58, 0.7: 0.96, 0.69: 0.26, 0.68: 0.47, 0.67: 0.86, 0.66: 0.25, 0.65: 0.22, 0.64: 0.98, 0.63: 0.79, 0.62: 0.35, 0.61: 0.93, 0.6: 0.83, 0.59: 0.77, 0.58: 0.22, 0.57: 0.79, 0.56: 0.24, 0.55: 0.37, 0.54: 0.9, 0.53: 0.49, 0.52: 0.79, 0.51: 0.09, 0.5: 0.11, 0.49: 0.87, 0.48: 0.22, 0.47: 0.23, 0.46: 0.51, 0.45: 0.82, 0.44: 0.59, 0.43: 0.23, 0.42: 0.14, 0.41: 0.49, 0.4: 0.02, 0.39: 0.22, 0.38: 0.55, 0.37: 0.78, 0.36: 0.16, 0.35: 0.25, 0.34: 0.13, 0.33: 0.37, 0.32: 0.82, 0.31: 0.67, 0.3: 0.3, 0.29: 0.38, 0.28: 0.19, 0.27: 0.66, 0.26: 0.46, 0.25: 0.81, 0.24: 0.35, 0.23: 0.06, 0.22: 0.43, 0.21: 0.01, 0.2: 0.02, 0.19: 0.17, 0.18: 0.95, 0.17: 0.19, 0.16: 0.18, 0.15: 0.82, 0.14: 0.94, 0.13: 0.68, 0.12: 0.29, 0.11: 0.35, 0.1: 0.2, 0.09: 0.61, 0.08: 0.51, 0.07: 0.25, 0.06: 0.84, 0.05: 0.0, 0.04: 0.49, 0.03: 0.38, 0.02: 0.33, 0.01: 0.92, 0.0: 0.58}, 'Jack': {1.0: 0.97, 0.99: 0.93, 0.98: 0.44, 0.97: 0.53, 0.96: 0.96, 0.95: 0.86, 0.94: 0.12, 0.93: 0.39, 0.92: 0.66, 0.91: 0.13, 0.9: 0.33, 0.89: 0.92, 0.88: 0.8, 0.87: 0.7, 0.86: 0.3, 0.85: 0.51, 0.84: 0.57, 0.83: 0.36, 0.82: 0.77, 0.81: 0.55, 0.8: 0.3, 0.79: 0.62, 0.78: 0.3, 0.77: 0.53, 0.76: 0.87, 0.75: 0.1, 0.74: 0.61, 0.73: 0.09, 0.72: 0.13, 0.71: 0.04, 0.7: 0.13, 0.69: 0.19, 0.68: 0.43, 0.67: 0.4, 0.66: 0.71, 0.65: 0.83, 0.64: 0.14, 0.63: 0.34, 0.62: 0.71, 0.61: 0.78, 0.6: 0.18, 0.59: 0.42, 0.58: 0.85, 0.57: 0.16, 0.56: 0.52, 0.55: 0.17, 0.54: 0.81, 0.53: 0.17, 0.52: 0.24, 0.51: 0.69, 0.5: 0.87, 0.49: 0.67, 0.48: 0.88, 0.47: 0.65, 0.46: 0.19, 0.45: 0.86, 0.44: 0.49, 0.43: 0.71, 0.42: 0.77, 0.41: 0.86, 0.4: 0.37, 0.39: 0.87, 0.38: 0.54, 0.37: 0.74, 0.36: 0.67, 0.35: 0.6, 0.34: 0.56, 0.33: 0.8, 0.32: 0.06, 0.31: 0.8, 0.3: 0.01, 0.29: 0.05, 0.28: 0.26, 0.27: 0.5, 0.26: 0.07, 0.25: 0.6, 0.24: 0.67, 0.23: 0.77, 0.22: 0.5, 0.21: 0.4, 0.2: 0.17, 0.19: 0.59, 0.18: 0.86, 0.17: 0.18, 0.16: 0.89, 0.15: 0.9, 0.14: 0.09, 0.13: 0.68, 0.12: 0.65, 0.11: 0.62, 0.1: 0.98, 0.09: 0.52, 0.08: 0.09, 0.07: 0.02, 0.06: 0.55, 0.05: 0.41, 0.04: 0.45, 0.03: 0.07, 0.02: 0.64, 0.01: 0.88, 0.0: 0.13}, 'Knight': {1.0: 0.42, 0.99: 0.4, 0.98: 0.75, 0.97: 0.36, 0.96: 0.76, 0.95: 0.66, 0.94: 0.09, 0.93: 0.37, 0.92: 0.05, 0.91: 0.95, 0.9: 0.02, 0.89: 0.39, 0.88: 0.46, 0.87: 0.25, 0.86: 0.67, 0.85: 0.71, 0.84: 0.93, 0.83: 0.27, 0.82: 1.0, 0.81: 0.22, 0.8: 0.61, 0.79: 0.93, 0.78: 0.8, 0.77: 0.99, 0.76: 0.88, 0.75: 0.34, 0.74: 0.39, 0.73: 0.81, 0.72: 0.05, 0.71: 0.39, 0.7: 0.72, 0.69: 0.11, 0.68: 0.29, 0.67: 0.31, 0.66: 0.81, 0.65: 0.09, 0.64: 0.67, 0.63: 0.41, 0.62: 0.94, 0.61: 0.1, 0.6: 0.25, 0.59: 0.81, 0.58: 0.91, 0.57: 0.36, 0.56: 0.27, 0.55: 0.31, 0.54: 0.99, 0.53: 0.59, 0.52: 0.76, 0.51: 0.61, 0.5: 0.08, 0.49: 0.07, 0.48: 0.3, 0.47: 0.26, 0.46: 0.13, 0.45: 0.76, 0.44: 0.04, 0.43: 0.92, 0.42: 0.56, 0.41: 0.27, 0.4: 0.77, 0.39: 0.32, 0.38: 0.54, 0.37: 0.99, 0.36: 0.92, 0.35: 0.33, 0.34: 0.38, 0.33: 0.62, 0.32: 0.61, 0.31: 0.15, 0.3: 0.01, 0.29: 0.61, 0.28: 0.67, 0.27: 0.12, 0.26: 0.9, 0.25: 0.45, 0.24: 0.89, 0.23: 0.71, 0.22: 0.68, 0.21: 0.44, 0.2: 0.58, 0.19: 0.55, 0.18: 0.32, 0.17: 0.39, 0.16: 0.34, 0.15: 0.0, 0.14: 0.48, 0.13: 0.77, 0.12: 0.46, 0.11: 0.61, 0.1: 0.25, 0.09: 0.98, 0.08: 0.9, 0.07: 0.7, 0.06: 0.83, 0.05: 0.73, 0.04: 0.35, 0.03: 0.39, 0.02: 0.73, 0.01: 0.06, 0.0: 0.7}, 'King': {1.0: 0.4, 0.99: 0.46, 0.98: 0.68, 0.97: 0.7, 0.96: 0.92, 0.95: 0.99, 0.94: 0.51, 0.93: 0.01, 0.92: 0.5, 0.91: 0.37, 0.9: 0.94, 0.89: 0.57, 0.88: 0.85, 0.87: 0.61, 0.86: 0.34, 0.85: 0.76, 0.84: 0.02, 0.83: 0.82, 0.82: 0.15, 0.81: 0.63, 0.8: 0.74, 0.79: 0.31, 0.78: 0.2, 0.77: 0.39, 0.76: 0.07, 0.75: 0.44, 0.74: 0.17, 0.73: 0.65, 0.72: 0.35, 0.71: 0.05, 0.7: 0.13, 0.69: 0.11, 0.68: 0.31, 0.67: 0.14, 0.66: 0.69, 0.65: 0.47, 0.64: 0.13, 0.63: 0.43, 0.62: 0.99, 0.61: 0.57, 0.6: 0.66, 0.59: 0.97, 0.58: 0.27, 0.57: 0.05, 0.56: 0.81, 0.55: 0.12, 0.54: 0.13, 0.53: 0.55, 0.52: 0.8, 0.51: 0.72, 0.5: 0.64, 0.49: 0.61, 0.48: 0.72, 0.47: 0.79, 0.46: 0.61, 0.45: 0.78, 0.44: 0.9, 0.43: 0.96, 0.42: 0.19, 0.41: 0.88, 0.4: 0.74, 0.39: 0.65, 0.38: 0.07, 0.37: 0.58, 0.36: 0.07, 0.35: 0.73, 0.34: 0.11, 0.33: 0.25, 0.32: 1.0, 0.31: 0.21, 0.3: 0.65, 0.29: 0.71, 0.28: 0.6, 0.27: 0.9, 0.26: 0.6, 0.25: 0.04, 0.24: 0.57, 0.23: 0.44, 0.22: 0.98, 0.21: 0.16, 0.2: 0.45, 0.19: 0.29, 0.18: 0.65, 0.17: 0.41, 0.16: 0.98, 0.15: 0.25, 0.14: 0.98, 0.13: 0.86, 0.12: 0.89, 0.11: 0.74, 0.1: 0.79, 0.09: 0.21, 0.08: 0.18, 0.07: 0.62, 0.06: 0.19, 0.05: 0.75, 0.04: 0.15, 0.03: 0.16, 0.02: 0.65, 0.01: 0.74, 0.0: 0.41}, '3': {1.0: 0.11, 0.99: 0.08, 0.98: 0.56, 0.97: 0.2, 0.96: 0.13, 0.95: 0.7, 0.94: 0.2, 0.93: 0.23, 0.92: 0.06, 0.91: 0.13, 0.9: 0.43, 0.89: 0.99, 0.88: 0.28, 0.87: 0.37, 0.86: 0.35, 0.85: 0.44, 0.84: 0.5, 0.83: 0.55, 0.82: 0.01, 0.81: 0.42, 0.8: 0.99, 0.79: 0.4, 0.78: 0.07, 0.77: 0.55, 0.76: 0.21, 0.75: 0.43, 0.74: 0.51, 0.73: 0.02, 0.72: 0.39, 0.71: 0.98, 0.7: 0.46, 0.69: 0.73, 0.68: 0.72, 0.67: 0.84, 0.66: 0.56, 0.65: 0.13, 0.64: 0.15, 0.63: 0.86, 0.62: 0.01, 0.61: 0.04, 0.6: 0.76, 0.59: 0.42, 0.58: 0.42, 0.57: 0.31, 0.56: 0.94, 0.55: 0.1, 0.54: 0.38, 0.53: 0.91, 0.52: 0.89, 0.51: 0.23, 0.5: 0.27, 0.49: 0.29, 0.48: 0.0, 0.47: 0.55, 0.46: 0.9, 0.45: 0.62, 0.44: 0.52, 0.43: 0.37, 0.42: 0.83, 0.41: 0.07, 0.4: 0.26, 0.39: 0.32, 0.38: 0.93, 0.37: 0.7, 0.36: 0.79, 0.35: 0.67, 0.34: 0.33, 0.33: 0.3, 0.32: 0.55, 0.31: 0.44, 0.3: 0.46, 0.29: 0.18, 0.28: 0.67, 0.27: 0.44, 0.26: 0.89, 0.25: 0.41, 0.24: 0.61, 0.23: 0.59, 0.22: 0.37, 0.21: 0.41, 0.2: 0.86, 0.19: 0.3, 0.18: 0.34, 0.17: 0.98, 0.16: 0.25, 0.15: 0.21, 0.14: 0.41, 0.13: 0.27, 0.12: 0.69, 0.11: 0.98, 0.1: 0.69, 0.09: 0.24, 0.08: 0.47, 0.07: 0.82, 0.06: 0.37, 0.05: 0.64, 0.04: 0.32, 0.03: 0.98, 0.02: 0.87, 0.01: 0.83, 0.0: 0.19}, '1': {1.0: 0.82, 0.99: 0.49, 0.98: 0.43, 0.97: 0.76, 0.96: 0.31, 0.95: 0.81, 0.94: 0.98, 0.93: 0.03, 0.92: 0.3, 0.91: 0.08, 0.9: 0.53, 0.89: 0.16, 0.88: 0.36, 0.87: 0.26, 0.86: 0.41, 0.85: 0.37, 0.84: 0.81, 0.83: 0.37, 0.82: 0.67, 0.81: 0.02, 0.8: 0.71, 0.79: 0.14, 0.78: 0.27, 0.77: 0.47, 0.76: 0.16, 0.75: 0.08, 0.74: 0.27, 0.73: 0.77, 0.72: 0.39, 0.71: 0.84, 0.7: 0.99, 0.69: 0.06, 0.68: 0.97, 0.67: 0.91, 0.66: 0.92, 0.65: 0.59, 0.64: 0.1, 0.63: 0.44, 0.62: 0.22, 0.61: 0.45, 0.6: 0.75, 0.59: 0.08, 0.58: 0.6, 0.57: 0.44, 0.56: 0.02, 0.55: 0.75, 0.54: 0.67, 0.53: 0.02, 0.52: 0.25, 0.51: 0.32, 0.5: 0.96, 0.49: 0.06, 0.48: 0.4, 0.47: 0.82, 0.46: 0.37, 0.45: 0.06, 0.44: 0.22, 0.43: 0.8, 0.42: 0.55, 0.41: 0.44, 0.4: 0.83, 0.39: 0.4, 0.38: 0.2, 0.37: 0.35, 0.36: 0.72, 0.35: 0.66, 0.34: 0.12, 0.33: 0.75, 0.32: 0.93, 0.31: 0.6, 0.3: 0.37, 0.29: 0.91, 0.28: 0.42, 0.27: 0.69, 0.26: 0.18, 0.25: 0.66, 0.24: 0.91, 0.23: 0.85, 0.22: 0.51, 0.21: 0.39, 0.2: 0.28, 0.19: 0.84, 0.18: 0.39, 0.17: 0.23, 0.16: 0.13, 0.15: 0.21, 0.14: 0.67, 0.13: 0.58, 0.12: 0.64, 0.11: 0.92, 0.1: 0.96, 0.09: 0.29, 0.08: 0.36, 0.07: 0.88, 0.06: 0.87, 0.05: 0.56, 0.04: 0.36, 0.03: 0.8, 0.02: 0.76, 0.01: 0.76, 0.0: 0.75}, 'brisJack': {1.0: 0.72, 0.99: 0.76, 0.98: 0.49, 0.97: 0.55, 0.96: 0.17, 0.95: 0.45, 0.94: 0.93, 0.93: 0.32, 0.92: 0.74, 0.91: 0.28, 0.9: 0.5, 0.89: 0.21, 0.88: 0.07, 0.87: 0.18, 0.86: 0.13, 0.85: 0.33, 0.84: 0.68, 0.83: 0.62, 0.82: 0.89, 0.81: 0.54, 0.8: 0.5, 0.79: 0.36, 0.78: 0.48, 0.77: 0.51, 0.76: 0.74, 0.75: 0.65, 0.74: 0.86, 0.73: 0.64, 0.72: 0.06, 0.71: 0.82, 0.7: 0.34, 0.69: 0.22, 0.68: 0.29, 0.67: 0.09, 0.66: 0.97, 0.65: 0.64, 0.64: 0.77, 0.63: 0.33, 0.62: 0.71, 0.61: 0.53, 0.6: 0.22, 0.59: 0.76, 0.58: 0.55, 0.57: 0.25, 0.56: 0.62, 0.55: 0.27, 0.54: 0.53, 0.53: 0.68, 0.52: 0.25, 0.51: 0.86, 0.5: 0.18, 0.49: 0.72, 0.48: 0.84, 0.47: 0.82, 0.46: 0.28, 0.45: 0.61, 0.44: 0.48, 0.43: 0.15, 0.42: 0.28, 0.41: 0.62, 0.4: 0.25, 0.39: 0.73, 0.38: 0.65, 0.37: 0.88, 0.36: 0.23, 0.35: 0.93, 0.34: 0.93, 0.33: 0.85, 0.32: 0.05, 0.31: 0.07, 0.3: 0.89, 0.29: 0.36, 0.28: 0.97, 0.27: 0.11, 0.26: 0.6, 0.25: 0.49, 0.24: 0.44, 0.23: 0.92, 0.22: 0.41, 0.21: 0.29, 0.2: 0.76, 0.19: 0.18, 0.18: 0.87, 0.17: 0.39, 0.16: 0.75, 0.15: 0.14, 0.14: 0.06, 0.13: 0.63, 0.12: 0.28, 0.11: 0.34, 0.1: 0.23, 0.09: 0.75, 0.08: 0.55, 0.07: 0.01, 0.06: 0.35, 0.05: 1.0, 0.04: 0.92, 0.03: 0.25, 0.02: 0.65, 0.01: 0.2, 0.0: 0.48}, 'brisKnight': {1.0: 0.36, 0.99: 0.42, 0.98: 0.97, 0.97: 0.51, 0.96: 0.35, 0.95: 0.19, 0.94: 0.83, 0.93: 0.95, 0.92: 0.96, 0.91: 0.93, 0.9: 0.56, 0.89: 0.71, 0.88: 0.25, 0.87: 0.5, 0.86: 0.25, 0.85: 0.92, 0.84: 0.01, 0.83: 0.86, 0.82: 0.8, 0.81: 0.24, 0.8: 0.89, 0.79: 0.18, 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         0.78: 0.92, 0.77: 0.17, 0.76: 0.2, 0.75: 0.36, 0.74: 0.4, 0.73: 0.92, 0.72: 0.47, 0.71: 0.52, 0.7: 0.5, 0.69: 0.64, 0.68: 0.45, 0.67: 0.03, 0.66: 0.25, 0.65: 0.1, 0.64: 0.64, 0.63: 0.84, 0.62: 0.86, 0.61: 0.22, 0.6: 0.45, 0.59: 0.57, 0.58: 0.29, 0.57: 0.07, 0.56: 0.23, 0.55: 0.02, 0.54: 0.35, 0.53: 0.67, 0.52: 0.81, 0.51: 0.03, 0.5: 0.52, 0.49: 0.37, 0.48: 0.39, 0.47: 0.43, 0.46: 0.73, 0.45: 0.01, 0.44: 0.5, 0.43: 0.48, 0.42: 0.94, 0.41: 0.88, 0.4: 0.65, 0.39: 0.54, 0.38: 0.22, 0.37: 0.53, 0.36: 0.6, 0.35: 0.96, 0.34: 0.69, 0.33: 0.73, 0.32: 0.13, 0.31: 0.11, 0.3: 0.95, 0.29: 0.64, 0.28: 0.66, 0.27: 0.19, 0.26: 0.19, 0.25: 0.68, 0.24: 0.15, 0.23: 0.61, 0.22: 0.7, 0.21: 0.96, 0.2: 0.63, 0.19: 0.76, 0.18: 0.51, 0.17: 0.26, 0.16: 0.05, 0.15: 0.76, 0.14: 0.76, 0.13: 0.71, 0.12: 0.57, 0.11: 0.12, 0.1: 0.77, 0.09: 0.26, 0.08: 0.48, 0.07: 0.31, 0.06: 0.39, 0.05: 0.77, 0.04: 0.62, 0.03: 0.72, 0.02: 0.48, 0.01: 0.57, 0.0: 0.25}, 'brisKing': {1.0: 0.36, 0.99: 0.42, 0.98: 0.97, 0.97: 0.51, 0.96: 0.35, 0.95: 0.19, 0.94: 0.83, 0.93: 0.95, 0.92: 0.96, 0.91: 0.93, 0.9: 0.56, 0.89: 0.71, 0.88: 0.25, 0.87: 0.5, 0.86: 0.25, 0.85: 0.92, 0.84: 0.01, 0.83: 0.86, 0.82: 0.8, 0.81: 0.24, 0.8: 0.89, 0.79: 0.18, 0.78: 0.92, 0.77: 0.17, 0.76: 0.2, 0.75: 0.36, 0.74: 0.4, 0.73: 0.92, 0.72: 0.47, 0.71: 0.52, 0.7: 0.5, 0.69: 0.64, 0.68: 0.45, 0.67: 0.03, 0.66: 0.25, 0.65: 0.1, 0.64: 0.64, 0.63: 0.84, 0.62: 0.86, 0.61: 0.22, 0.6: 0.45, 0.59: 0.57, 0.58: 0.29, 0.57: 0.07, 0.56: 0.23, 0.55: 0.02, 0.54: 0.35, 0.53: 0.67, 0.52: 0.81, 0.51: 0.03, 0.5: 0.52, 0.49: 0.37, 0.48: 0.39, 0.47: 0.43, 0.46: 0.73, 0.45: 0.01, 0.44: 0.5, 0.43: 0.48, 0.42: 0.94, 0.41: 0.88, 0.4: 0.65, 0.39: 0.54, 0.38: 0.22, 0.37: 0.53, 0.36: 0.6, 0.35: 0.96, 0.34: 0.69, 0.33: 0.73, 0.32: 0.13, 0.31: 0.11, 0.3: 0.95, 0.29: 0.64, 0.28: 0.66, 0.27: 0.19, 0.26: 0.19, 0.25: 0.68, 0.24: 0.15, 0.23: 0.61, 0.22: 0.7, 0.21: 0.96, 0.2: 0.63, 0.19: 0.76, 0.18: 0.51, 0.17: 0.26, 0.16: 0.05, 0.15: 0.76, 0.14: 0.76, 0.13: 0.71, 0.12: 0.57, 0.11: 0.12, 0.1: 0.77, 0.09: 0.26, 0.08: 0.48, 0.07: 0.31, 0.06: 0.39, 0.05: 0.77, 0.04: 0.62, 0.03: 0.72, 0.02: 0.48, 0.01: 0.57, 0.0: 0.25}, 'bris3': {1.0: 0.52, 0.99: 0.04, 0.98: 0.07, 0.97: 0.87, 0.96: 0.17, 0.95: 0.49, 0.94: 0.09, 0.93: 0.28, 0.92: 0.58, 0.91: 0.87, 0.9: 1.0, 0.89: 0.99, 0.88: 0.4, 0.87: 0.08, 0.86: 0.18, 0.85: 0.21, 0.84: 0.42, 0.83: 0.97, 0.82: 0.89, 0.81: 0.3, 0.8: 0.29, 0.79: 0.92, 0.78: 0.4, 0.77: 0.6, 0.76: 0.8, 0.75: 0.68, 0.74: 0.5, 0.73: 0.66, 0.72: 0.85, 0.71: 0.07, 0.7: 0.91, 0.69: 0.99, 0.68: 0.07, 0.67: 0.84, 0.66: 0.17, 0.65: 0.73, 0.64: 0.35, 0.63: 0.97, 0.62: 0.67, 0.61: 0.59, 0.6: 0.01, 0.59: 0.43, 0.58: 0.48, 0.57: 0.85, 0.56: 0.44, 0.55: 0.21, 0.54: 0.03, 0.53: 0.33, 0.52: 0.03, 0.51: 0.3, 0.5: 0.71, 0.49: 0.15, 0.48: 0.83, 0.47: 0.66, 0.46: 0.11, 0.45: 0.67, 0.44: 0.07, 0.43: 0.64, 0.42: 0.93, 0.41: 0.86, 0.4: 0.87, 0.39: 0.71, 0.38: 0.3, 0.37: 0.6, 0.36: 0.17, 0.35: 0.64, 0.34: 0.39, 0.33: 0.35, 0.32: 0.4, 0.31: 0.71, 0.3: 0.29, 0.29: 0.16, 0.28: 0.7, 0.27: 0.65, 0.26: 0.35, 0.25: 0.78, 0.24: 0.42, 0.23: 0.67, 0.22: 0.63, 0.21: 0.58, 0.2: 0.58, 0.19: 0.89, 0.18: 0.24, 0.17: 0.37, 0.16: 0.34, 0.15: 0.0, 0.14: 0.77, 0.13: 0.79, 0.12: 0.27, 0.11: 0.0, 0.1: 0.91, 0.09: 0.73, 0.08: 0.13, 0.07: 0.48, 0.06: 0.66, 0.05: 0.7, 0.04: 0.51, 0.03: 0.13, 0.02: 0.1, 0.01: 0.24, 0.0: 0.86}, 'bris1': {1.0: 0.1, 0.99: 0.17, 0.98: 0.93, 0.97: 0.97, 0.96: 0.29, 0.95: 0.23, 0.94: 0.66, 0.93: 0.18, 0.92: 0.62, 0.91: 0.8, 0.9: 0.17, 0.89: 0.69, 0.88: 0.81, 0.87: 0.54, 0.86: 1.0, 0.85: 0.84, 0.84: 0.09, 0.83: 0.08, 0.82: 0.83, 0.81: 0.13, 0.8: 0.22, 0.79: 0.78, 0.78: 0.09, 0.77: 0.13, 0.76: 0.1, 0.75: 0.26, 0.74: 0.99, 0.73: 0.03, 0.72: 0.11, 0.71: 0.75, 0.7: 0.51, 0.69: 0.35, 0.68: 0.84, 0.67: 0.55, 0.66: 0.36, 0.65: 0.98, 0.64: 0.67, 0.63: 0.7, 0.62: 0.95, 0.61: 0.86, 0.6: 0.03, 0.59: 0.36, 0.58: 0.27, 0.57: 0.25, 0.56: 0.78, 0.55: 0.3, 0.54: 0.34, 0.53: 0.61, 0.52: 0.84, 0.51: 0.46, 0.5: 0.16, 0.49: 0.97, 0.48: 0.26, 0.47: 0.09, 0.46: 0.1, 0.45: 0.9, 0.44: 0.1, 0.43: 0.98, 0.42: 0.14, 0.41: 0.09, 0.4: 0.43, 0.39: 0.67, 0.38: 0.49, 0.37: 0.17, 0.36: 0.84, 0.35: 0.51, 0.34: 0.18, 0.33: 0.01, 0.32: 0.61, 0.31: 0.82, 0.3: 0.74, 0.29: 0.09, 0.28: 0.72, 0.27: 0.35, 0.26: 0.7, 0.25: 0.39, 0.24: 0.66, 0.23: 0.19, 0.22: 0.06, 0.21: 0.4, 0.2: 0.33, 0.19: 0.33, 0.18: 0.29, 0.17: 0.02, 0.16: 0.4, 0.15: 0.87, 0.14: 0.5, 0.13: 0.71, 0.12: 0.37, 0.11: 0.39, 0.1: 0.79, 0.09: 0.16, 0.08: 0.31, 0.07: 0.96, 0.06: 0.3, 0.05: 0.99, 0.04: 0.6, 0.03: 0.88, 0.02: 0.43, 0.01: 0.79, 0.0: 0.54}})]
    briscola = ""
    deck = []
    print("Hi")
    game = Game(briscola, deck, players)
    winner = game.play(briscola, deck, players)
    i += 1
    if winner == "Model":
        AgentWins += 1
    if winner == "Simple":
        AgentLosses += 1
    if winner == "tie":
        AgentTies += 1
sys.stdout = sys.__stdout__
print("AI wins: " + str(AgentWins))
print("AI losses: " + str(AgentLosses))
print("Ties: " + str(AgentTies))