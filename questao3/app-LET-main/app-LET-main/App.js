import React from "react";
import { View, Text} from "react-native";
import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import {Entypo, Feather} from '@expo/vector-icons';

import home from './home/home.js'
import atividades from './atividades/atividade.js';
import camera from './camera/camera.js';
import perfil from './perfil/perfil.js';
import relatorio from './relatorio/relatorio.js';

const Stack = createStackNavigator();
const Tab = createBottomTabNavigator();

function Tabs() {
  return(
    <Tab.Navigator 
    screenOptions={{
      tabBarStyle: {
        backgroundColor: '#91C1EF',
        borderTopColor: 'transparent',
        paddingBottom: 5,
        paddingTop:5,
      },
      tabBarActiveTintColor: '#FFF',
      
    }}>
      <Tab.Screen 
      name="Início" 
      component={home}
      options={{
        tabBarIcon: ({ size, color}) => (
          <Entypo name="home" size={size} color={color} />
        )
      }}
      />
      <Tab.Screen 
      name="Tarefas" 
      component={atividades}
      options={{
        tabBarIcon: ({ size, color}) => (
          <Feather name="list" size={size} color={color} />
        )
      }}
      />
      <Tab.Screen 
      name="Câmera" 
      component={camera}
      options={{
        tabBarIcon: ({ size, color}) => (
          <Feather name="video" size={size} color={color} />
        )
      }}
      />
      <Tab.Screen 
      name="Relatório" 
      component={relatorio}
      options={{
        tabBarIcon: ({ size, color}) => (
          <Feather name="clipboard" size={size} color={color} />
        )
      }}
      />
      <Tab.Screen 
      name="Perfil" 
      component={perfil}
      options={{
        tabBarIcon: ({ size, color}) => (
          <Feather name="user" size={size} color={color} />
        )
      }}/>
    </Tab.Navigator>
  );
}

export default function App() {
  return(
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen 
        name="Home" 
        component={Tabs}
        options={{
          title: 'LIFE EDGE TECHNOLOGIES',
          headerStyle: {
            backgroundColor: '#91C1EF'
          },
          headerTintColor: '#FFF'
        }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}