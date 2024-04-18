import React from 'react';
import { View, Text, StyleSheet, ScrollView} from 'react-native';

export default function perfil() {
    return (
        <ScrollView>
            <View style={styles.container}>
                <View style={styles.quadrados}>
                    <Text style={styles.header}> Usuário </Text>
                    <Text style={styles.text}> xxxxxxx@yyyyy </Text>
                </View>
                <View style={styles.quadrado2}>
                    <Text style={styles.header}> Pacientes cadastrados: </Text>
                    <Text style={styles.text}> - xxxxxxx </Text>
                    <Text style={styles.text}> - yyyyyyy </Text>
                </View>
                <View style={styles.quadrado2}>
                    <Text style={styles.header}> Notificações: </Text>
                    <Text style={styles.text}> - xxxxxxx </Text>
                    <Text style={styles.text}> - yyyyyyy </Text>
                </View>
                <View style={styles.quadrado2}>
                    <Text style={styles.header}> Profissionais cadastrados: </Text>
                    <Text style={styles.text}> - xxxxxxx@yyy </Text>
                    <Text style={styles.text}> - yyyyyyy@zzz </Text>
                </View>
            </View>
        </ScrollView>
    );
}

const styles = StyleSheet.create({
    header: {
        fontSize: 15,
        marginBottom: 10,
    },
    text: {
        fontSize: 12,
    },
    quadrados: {
        paddingVertical: 15,
        paddingHorizontal: 15,
        margin: '1%',
        borderRadius:8,
        borderColor: '#C0C0C0',
        backgroundColor: '#DCDCDC',
        borderWidth: 1,
        width: '98%',
        height: 80,
    },
    quadrado2: {
        paddingVertical: 15,
        paddingHorizontal: 15,
        margin: '1%',
        borderRadius:8,
        borderColor: '#C0C0C0',
        backgroundColor: '#DCDCDC',
        borderWidth: 1,
        width: '98%',
        height: 100,
    },
})