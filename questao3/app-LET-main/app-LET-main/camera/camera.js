import React from 'react';
import { View, Text, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStacknavigator } from '@react-navigation/stack';

export default function camera() {
    return (
        <View>
            <Text> camera </Text>
        </View>
    );
}

{/*const Stack = createStacknavigator();*/}

{/*import camera1 from './camera/camera1.js';
import camera2 from './camera/camera2.js';*/}

{/*export default function camera() {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen name="Câmera 1" component={camera1}/>
                <Stack.Screen name="Câmera 2" component={camera2}/>
            </Stack.Navigator>
        </NavigationContainer>
    );
}*/}

{/*export default function botao({navigation}){
    return(
        <View>
            <button
            title="Câmera 1"
            onPress={ () => navigation.navigate('camera1')}
            />
            <button
            title="Câmera 2"
            onPress={ () => navigation.navigate('camera2')}
            />
        </View>
    )
}*/}