#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de IMC (Índice de Massa Corporal)
Desenvolvido por: Thais Maximiana
Data: 2024
"""

import sys
from typing import Tuple, Optional


class IMCCalculator:
    """
    Classe para cálculo e classificação do IMC
    """
    
    def __init__(self):
        self.classificacoes = {
            (0, 18.5): "Abaixo do peso",
            (18.5, 25): "Peso normal",
            (25, 30): "Sobrepeso",
            (30, 35): "Obesidade grau I",
            (35, 40): "Obesidade grau II",
            (40, float('inf')): "Obesidade grau III"
        }
    
    def calcular_imc(self, peso: float, altura: float) -> float:
        """
        Calcula o IMC baseado no peso e altura
        
        Args:
            peso (float): Peso em quilogramas
            altura (float): Altura em metros
            
        Returns:
            float: Valor do IMC
            
        Raises:
            ValueError: Se os valores forem inválidos
        """
        if peso <= 0:
            raise ValueError("Peso deve ser maior que zero")
        if altura <= 0:
            raise ValueError("Altura deve ser maior que zero")
        if altura > 3.0:
            raise ValueError("Altura deve ser menor que 3 metros")
        if peso > 500:
            raise ValueError("Peso deve ser menor que 500 kg")
            
        return round(peso / (altura ** 2), 2)
    
    def classificar_imc(self, imc: float) -> str:
        """
        Classifica o IMC conforme padrões da OMS
        
        Args:
            imc (float): Valor do IMC
            
        Returns:
            str: Classificação do IMC
        """
        for (min_val, max_val), classificacao in self.classificacoes.items():
            if min_val <= imc < max_val:
                return classificacao
        return "Classificação não encontrada"
    
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


def validar_entrada(valor: str, tipo: str) -> float:
    """
    Valida e converte entrada do usuário
    
    Args:
        valor (str): Valor inserido pelo usuário
        tipo (str): Tipo de valor ('peso' ou 'altura')
        
    Returns:
        float: Valor convertido
        
    Raises:
        ValueError: Se a entrada for inválida
    """
    try:
        valor_float = float(valor.replace(',', '.'))
        if valor_float <= 0:
            raise ValueError(f"{tipo.capitalize()} deve ser maior que zero")
        return valor_float
    except ValueError as e:
        if "could not convert" in str(e):
            raise ValueError(f"Por favor, insira um {tipo} válido (números apenas)")
        raise


def obter_dados_usuario() -> Tuple[float, float]:
    """
    Obtém peso e altura do usuário com validação
    
    Returns:
        Tuple[float, float]: (peso, altura)
    """
    print("=" * 50)
    print("🏥 CALCULADORA DE IMC 🏥")
    print("=" * 50)
    print()
    
    while True:
        try:
            peso_str = input("📏 Digite seu peso em kg: ").strip()
            peso = validar_entrada(peso_str, "peso")
            break
        except ValueError as e:
            print(f"❌ Erro: {e}")
            print("Tente novamente...\n")
    
    while True:
        try:
            altura_str = input("📐 Digite sua altura em metros (ex: 1.75): ").strip()
            altura = validar_entrada(altura_str, "altura")
            break
        except ValueError as e:
            print(f"❌ Erro: {e}")
            print("Tente novamente...\n")
    
    return peso, altura


def exibir_resultado(imc: float, classificacao: str, recomendacao: str):
    """
    Exibe o resultado do cálculo de forma formatada
    
    Args:
        imc (float): Valor do IMC
        classificacao (str): Classificação do IMC
        recomendacao (str): Recomendação
    """
    print("\n" + "=" * 50)
    print("📊 RESULTADO DO SEU IMC")
    print("=" * 50)
    print(f"🎯 Seu IMC é: {imc}")
    print(f"📋 Classificação: {classificacao}")
    print(f"💡 Recomendação: {recomendacao}")
    print("=" * 50)
    
    # Tabela de referência
    print("\n📚 TABELA DE REFERÊNCIA (OMS):")
    print("-" * 30)
    print("IMC < 18.5     → Abaixo do peso")
    print("18.5 ≤ IMC < 25 → Peso normal")
    print("25 ≤ IMC < 30   → Sobrepeso")
    print("30 ≤ IMC < 35   → Obesidade grau I")
    print("35 ≤ IMC < 40   → Obesidade grau II")
    print("IMC ≥ 40        → Obesidade grau III")


def main():
    """
    Função principal do programa
    """
    try:
        # Criar instância da calculadora
        calculadora = IMCCalculator()
        
        # Obter dados do usuário
        peso, altura = obter_dados_usuario()
        
        # Calcular IMC
        imc = calculadora.calcular_imc(peso, altura)
        
        # Classificar IMC
        classificacao = calculadora.classificar_imc(imc)
        
        # Obter recomendação
        recomendacao = calculadora.obter_recomendacao(imc)
        
        # Exibir resultado
        exibir_resultado(imc, classificacao, recomendacao)
        
        # Perguntar se deseja calcular novamente
        while True:
            continuar = input("\n🔄 Deseja calcular outro IMC? (s/n): ").strip().lower()
            if continuar in ['s', 'sim', 'y', 'yes']:
                print("\n" + "=" * 50)
                main()
                break
            elif continuar in ['n', 'não', 'nao', 'no']:
                print("\n👋 Obrigado por usar a Calculadora de IMC!")
                print("💪 Mantenha-se saudável!")
                break
            else:
                print("❌ Por favor, responda 's' para sim ou 'n' para não")
        
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("Por favor, tente novamente.")
        sys.exit(1)


if __name__ == "__main__":
    main()
