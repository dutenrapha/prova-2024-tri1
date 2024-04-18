import React from 'react';
import {View, Text, StyleSheet, ScrollView} from 'react-native';

{/*const DisplayAnImage = () => {
    return(
        <Image
            style={styles.logo1}
            source={{
                uri: 'https://media-public.canva.com/c7TPQ/MAFzskc7TPQ/1/tl.png',
            }}
        />
    )
}    */}

export default function home({ navigation }) {
    return (
        <ScrollView>
            <View style={styles.container}>
                <View style={[styles.quadrados, styles.q1]}>
                    <Text style={styles.header}> O que é o Alzheimer? </Text>
                    <Text style={styles.text}> A Doença de Alzheimer é uma condição em que o cérebro começa a funcionar mal, resultando em problemas de memória, dificuldade para realizar atividades cotidianas e mudanças de comportamento. Isso acontece porque algumas proteínas no cérebro não são processadas corretamente, formando substâncias tóxicas que danificam as células cerebrais. Isso leva à perda gradual de células em áreas importantes do cérebro responsáveis pela memória, linguagem, raciocínio e outras funções mentais. </Text>
                </View>
                <View style={[styles.quadrados, styles.q2]}>
                    <Text style={styles.header}> Os estágios do Alzheimer: </Text>
                    <Text style={styles.text}> No estágio inicial, ocorrem mudanças na memória, na personalidade e nas habilidades visuais e espaciais. </Text>
                    <Text style={styles.text}> No estágio moderado, há dificuldade para falar, fazer tarefas simples e coordenar movimentos. Pode haver agitação e insônia. </Text>
                    <Text style={styles.text}> No estágio grave, a pessoa tem dificuldade em fazer tarefas diárias, como se vestir ou se alimentar. Também pode ocorrer incontinência urinária e fecal, e a mobilidade fica muito comprometida. </Text>
                    <Text style={styles.text}> No estágio terminal, a pessoa fica restrita ao leito, não fala mais, tem dificuldade para engolir e está mais suscetível a infecções. </Text>
                </View>
                <View style={[styles.quadrados, styles.q3]}>
                    <Text style={styles.header}> Os sintomas do Alzheimer: </Text>
                    <Text style={styles.text}> Esquecer coisas que aconteceram recentemente.</Text>
                    <Text style={styles.text}> Fazer a mesma pergunta várias vezes.</Text>
                    <Text style={styles.text}> Ter dificuldade para acompanhar conversas complicadas ou pensamentos.</Text>
                    <Text style={styles.text}> Não conseguir resolver problemas simples.</Text>
                    <Text style={styles.text}> Ter problemas ao dirigir ou se perder em lugares familiares.</Text>
                    <Text style={styles.text}> Ter dificuldade em encontrar palavras para expressar pensamentos ou sentimentos.</Text>
                    <Text style={styles.text}> Mudanças de humor, como irritabilidade, suspeitas injustificadas, agressividade ou passividade, e se afastar das interações sociais.</Text>
                </View>
            </View>
        </ScrollView>
    );
}

const styles = StyleSheet.create({
    header: {
        fontSize: 20,
        marginBottom: 10,
    },
    text: {
        fontSize: 15,
    },
    quadrados: {
        paddingVertical: 15,
        paddingHorizontal: 15,
        margin: '1%',
        borderRadius:8,
        borderColor: '#C0C0C0',
        borderWidth: 1,
        width: '98%',
        height: 200,
    },
    q1: {
        backgroundColor: '#FFCCFF',
    },
    q2: {
        backgroundColor: '#CCCCFF',
    },
    q3: {
        backgroundColor: '#CCFFCC',
    },
    logo1: {
        width: 50,
        height: 50,

      },
});
