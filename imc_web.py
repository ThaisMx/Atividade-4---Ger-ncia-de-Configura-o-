#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de IMC - Versão Web
Desenvolvido por: Thais Maximiana
Data: 2024
"""

from flask import Flask, render_template, request, jsonify
import json
from typing import Dict, Any

app = Flask(__name__)


class IMCCalculatorWeb:
    """
    Classe para cálculo e classificação do IMC - Versão Web
    """
    
    def __init__(self):
        self.classificacoes = {
            (0, 18.5): {
                "nome": "Abaixo do peso",
                "cor": "warning",
                "icone": "⚠️"
            },
            (18.5, 25): {
                "nome": "Peso normal",
                "cor": "success",
                "icone": "✅"
            },
            (25, 30): {
                "nome": "Sobrepeso",
                "cor": "warning",
                "icone": "⚠️"
            },
            (30, 35): {
                "nome": "Obesidade grau I",
                "cor": "danger",
                "icone": "🔴"
            },
            (35, 40): {
                "nome": "Obesidade grau II",
                "cor": "danger",
                "icone": "🔴"
            },
            (40, float('inf')): {
                "nome": "Obesidade grau III",
                "cor": "danger",
                "icone": "🔴"
            }
        }
    
    def calcular_imc(self, peso: float, altura: float) -> float:
        """
        Calcula o IMC baseado no peso e altura
        
        Args:
            peso (float): Peso em quilogramas
            altura (float): Altura em metros
            
        Returns:
            float: Valor do IMC
        """
        if peso <= 0 or altura <= 0:
            raise ValueError("Peso e altura devem ser maiores que zero")
        if altura > 3.0:
            raise ValueError("Altura deve ser menor que 3 metros")
        if peso > 500:
            raise ValueError("Peso deve ser menor que 500 kg")
            
        return round(peso / (altura ** 2), 2)
    
    def classificar_imc(self, imc: float) -> Dict[str, Any]:
        """
        Classifica o IMC conforme padrões da OMS
        
        Args:
            imc (float): Valor do IMC
            
        Returns:
            Dict: Informações da classificação
        """
        for (min_val, max_val), info in self.classificacoes.items():
            if min_val <= imc < max_val:
                return info
        return {
            "nome": "Classificação não encontrada",
            "cor": "secondary",
            "icone": "❓"
        }
    
    def obter_recomendacao(self, imc: float) -> str:
        """
        Retorna recomendações baseadas no IMC
        
        Args:
            imc (float): Valor do IMC
            
        Returns:
            str: Recomendação
        """
        if imc < 18.5:
            return "Consulte um nutricionista para ganho de peso saudável"
        elif 18.5 <= imc < 25:
            return "Parabéns! Mantenha seus hábitos saudáveis"
        elif 25 <= imc < 30:
            return "Considere uma dieta balanceada e exercícios regulares"
        else:
            return "Recomendamos consulta médica para acompanhamento"


# Instância global da calculadora
calculadora = IMCCalculatorWeb()


@app.route('/')
def index():
    """
    Página principal da aplicação
    """
    return render_template('index.html')


@app.route('/calcular', methods=['POST'])
def calcular_imc():
    """
    Endpoint para cálculo do IMC via AJAX
    """
    try:
        data = request.get_json()
        peso = float(data.get('peso', 0))
        altura = float(data.get('altura', 0))
        
        # Validar entrada
        if peso <= 0 or altura <= 0:
            return jsonify({
                'sucesso': False,
                'erro': 'Peso e altura devem ser maiores que zero'
            }), 400
        
        if altura > 3.0:
            return jsonify({
                'sucesso': False,
                'erro': 'Altura deve ser menor que 3 metros'
            }), 400
        
        if peso > 500:
            return jsonify({
                'sucesso': False,
                'erro': 'Peso deve ser menor que 500 kg'
            }), 400
        
        # Calcular IMC
        imc = calculadora.calcular_imc(peso, altura)
        classificacao = calculadora.classificar_imc(imc)
        recomendacao = calculadora.obter_recomendacao(imc)
        
        return jsonify({
            'sucesso': True,
            'imc': imc,
            'classificacao': classificacao,
            'recomendacao': recomendacao
        })
        
    except ValueError as e:
        return jsonify({
            'sucesso': False,
            'erro': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': f'Erro interno: {str(e)}'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
