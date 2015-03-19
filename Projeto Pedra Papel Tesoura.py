# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 08:18:22 2015

@author: Felipe
"""

from random import randint
print('----------------------------------------------------------------------')
print('----------------------------------------------------------------------')
print('JOGO DE PEDRA, PAPEL, TESOURA, LAGARTO E SPOCK')
print('----------------------------------------------------------------------')
print('----------------------------------------------------------------------')
modo=int(input('QUAL MODO DE JOGO QUER JOGAR? 1 - SINGLE PLAYER; 2 - MULTIPLAYER - '))
if modo==1:
    print('0 - pedra, 1 - tesoura, 2 - papel, 3 - Spock, 4 - lagarto')
    i=0
    cpu=0
    ply=0
    while i<5:
        p1=int(input('P1 - ESCOLHA UMA JOGADA - '))
        p2=randint(0,4)
        if p1==p2:
            print('EMPATOU')
            print('OS DOIS ESCOLHERAM O MESMO')
        if p1==0 and p2==1:
            print('VC ESCOLHEU PEDRA')
            print('E O COMPUTADOR ESCOLHEU TESOURA')
            print('GANHOU - PEDRA ESMAGA TESOURA')
            ply+=1
        if p1==0 and p2==2:
            print('VC ESCOLHEU PEDRA')
            print('E O COMPUTADOR ESCOLHEU PAPEL')
            print('PERDEU - PAPEL EMBRULHA PEDRA')
            cpu+=1
        if p1==0 and p2==3:
            print('VC ESCOLHEU PEDRA')
            print('E O COMPUTADOR ESCOLHEU O SPOCK')
            print('PERDEU - SPOCK VAPORIZA A PEDRA')
            cpu+=1
        if p1==0 and p2==4:
            print('VC ESCOLHEU PEDRA')
            print('E O COMPUTADOR ESCOLHEU O LAGARTO')
            print('GANHOU - PEDRA ESMAGA O LAGARTO')
            ply+=1
        if p1==1 and p2==0:
            print('VC ESCOLHEU TESOURA')
            print('E O COMPUTADOR ESCOLHEU PEDRA')
            print('PERDEU - PEDRA ESMAGA TESOURA')
            cpu+=1
        if p1==1 and p2==2:
            print('VC ESCOLHEU TESOURA')
            print('E O COMPUTADOR ESCOLHEU PAPEL')
            print('GANHOU - TESOURA CORTA PAPEL')
            ply+=1
        if p1==1 and p2==3:
            print('VC ESCOLHEU TESOURA')
            print('E O COMPUTADOR ESCOLHEU O SPOCK')
            print('PERDEU - O SPOCK AMASSA A TESOURA')
            cpu+=1
        if p1==1 and p2==4:
            print('VC ESCOLHEU TESOURA')
            print('E O COMPUTADOR ESCOLHEU O LAGARTO')
            print('GANHOU - TESOURA CORTA A CABEÇA DO LAGARTO')
            ply+=1
        if p1==2 and p2==0:
            print('VC ESCOLHEU PAPEL')
            print('E O COMPUTADOR ESCOLHEU PEDRA')
            print('GANHOU - PAPEL EMBRULHA PEDRA')
            ply+=1
        if p1==2 and p2==1:
            print('VC ESCOLHEU PAPEL')
            print('E O COMPUTADOR ESCOLHEU TESOURA')
            print('PERDEU - TESOURA CORTA PAPEL')
            cpu+=1
        if p1==2 and p2==3:
            print('VC ESCOLHEU PAPEL')
            print('E O COMPUTADOR ESCOLHEU O SPOCK')
            print('GANHOU - SPOCK NAO SABE PREENCHER FORMULARIOS')
            ply+=1
        if p1==2 and p2==4:
            print('VC ESCOLHEU PAPEL')
            print('E O COMPUTADOR ESCOLHEU O LAGARTO')
            print('PERDEU - O LAGARTO COME PAPEL')
            cpu+=1
        if p1==3 and p2==0:
            print('VC ESCOLHEU O SPOCK')
            print('E O COMPUTADOR ESCOLHEU PEDRA')
            print('GANHOU - SPOCK VAPORIZA PEDRA')
            ply+=1
        if p1==3 and p2==2:
            print('VC ESCOLHEU O SPOCK')
            print('E O COMPUTADOR ESCOLHEU PAPEL')
            print('PERDEU - SPOCK NAO SABE PREENCHER FORMULARIOS')
            cpu+=1
        if p1==3 and p2==1:
            print('VC ESCOLHEU O SPOCK')
            print('E O COMPUTADOR ESCOLHEU TESOURA')
            print('GANHOU - SPOCK AMASSA TESOURA')
            ply+=1
        if p1==3 and p2==4:
            print('VC ESCOLHEU O SPOCK')
            print('E O COMPUTADOR ESCOLHEU O LAGARTO')
            print('PERDEU - O LAGARTO ENVENENA O SPOCK')
            cpu+=1
        if p1==4 and p2==0:
            print('VC ESCOLHEU O LAGARTO')
            print('E O COMPUTADOR ESCOLHEU PEDRA')
            print('PERDEU - PEDRA AMASSA O LAGARTO')
            cpu+=1
        if p1==4 and p2==1:
            print('VC ESCOLHEU O LAGARTO')
            print('E O COMPUTADOR ESCOLHEU TESOURA')
            print('PERDEU - TESOURA CORTA A CABEÇA DO LAGARTO')
            cpu+=1
        if p1==4 and p2==2:
            print('VC ESCOLHEU O LAGARTO')
            print('E O COMPUTADOR ESCOLHEU PAPEL')
            print('GANHOU - O LAGARTO COME O PAPEL')
            ply+=1
        if p1==4 and p2==3:
            print('VC ESCOLHEU O LAGARTO')
            print('E O COMPUTADOR ESCOLHEU O SPOCK')
            print('GANHOU - O LAGARTO ENVENENA O SPOCK')
            ply+=1
        i+=1
        print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    print('SEU SCORE FOI')
    print(ply)
    print('O SCORE DO OPONENTE FOI')
    print(cpu)
    if cpu>ply:
        print('VC PERDEU')
    elif cpu<ply:
        print('VC GANHOU')
    elif cpu==ply:
        print('EMPATOU')
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    
if modo==2:
    print('JOGADOR 1 USA AS TECLAS 0(pedra),1(tesoura),2(papel),3(Spock) E 4(lagarto)')
    print('JOGADOR 2 USA AS TECLAS 5(pedra),6(tesoura),7(papel),8(Spock) E 9(lagarto)')
    j=0
    j1=0
    j2=0
    while j<5:
        pl1=int(input('J1 - ESCOLHA UMA JOGADA - '))
        pl2=int(input('J2 - ESCOLHA UMA JOGADA - '))
        if pl1==0 and pl2==6:
            print('J1 ESCOLHEU PEDRA')
            print('E O J2 ESCOLHEU TESOURA')
            print('J1 GANHOU - PEDRA ESMAGA TESOURA')
            j1+=1
        if pl1==0 and pl2==7:
            print('J1 ESCOLHEU PEDRA')
            print('E O J2 ESCOLHEU PAPEL')
            print('J2 GANHOU - PAPEL EMBRULHA PEDRA')
            j2+=1
        if pl1==0 and pl2==8:
            print('J1 ESCOLHEU PEDRA')
            print('E O J2 ESCOLHEU O SPOCK')
            print('J2 GANHOU - SPOCK VAPORIZA A PEDRA')
            j2+=1
        if pl1==0 and pl2==9:
            print('J1 ESCOLHEU PEDRA')
            print('E O J2 ESCOLHEU O LAGARTO')
            print('J1 GANHOU - PEDRA ESMAGA O LAGARTO')
            j1+=1
        if pl1==1 and pl2==5:
            print('J1 ESCOLHEU TESOURA')
            print('E O J2 ESCOLHEU PEDRA')
            print('J2 GANHOU - PEDRA ESMAGA TESOURA')
            j2+=1
        if pl1==1 and pl2==7:
            print('J1 ESCOLHEU TESOURA')
            print('E O J2 ESCOLHEU PAPEL')
            print('J1 GANHOU - TESOURA CORTA PAPEL')
            j1+=1
        if pl1==1 and pl2==8:
            print('J1 ESCOLHEU TESOURA')
            print('E O J2 ESCOLHEU O SPOCK')
            print('J2 GANHOU - O SPOCK AMASSA A TESOURA')
            j2+=1
        if pl1==1 and pl2==9:
            print('J1 ESCOLHEU TESOURA')
            print('E O J2 ESCOLHEU O LAGARTO')
            print('J1 GANHOU - TESOURA CORTA A CABEÇA DO LAGARTO')
            j1+=1
        if pl1==2 and pl2==5:
            print('J1 ESCOLHEU PAPEL')
            print('E O J2 ESCOLHEU PEDRA')
            print('J1 GANHOU - PAPEL EMBRULHA PEDRA')
            j1+=1
        if pl1==2 and pl2==6:
            print('J1 ESCOLHEU PAPEL')
            print('E O J2 ESCOLHEU TESOURA')
            print('J2 GANHOU - TESOURA CORTA PAPEL')
            j2+=1
        if pl1==2 and pl2==8:
            print('J1 ESCOLHEU PAPEL')
            print('E O J2 ESCOLHEU O SPOCK')
            print('J1 GANHOU - SPOCK NAO SABE PREENCHER FORMULARIOS')
            j1+=1
        if pl1==2 and pl2==9:
            print('J1 ESCOLHEU PAPEL')
            print('E O J2 ESCOLHEU O LAGARTO')
            print('J2 GANHOU - O LAGARTO COME PAPEL')
            j2+=1
        if pl1==3 and pl2==5:
            print('J1 ESCOLHEU O SPOCK')
            print('E O J2 ESCOLHEU PEDRA')
            print('J1 GANHOU - SPOCK VAPORIZA PEDRA')
            j1+=1
        if pl1==3 and pl2==7:
            print('J1 ESCOLHEU O SPOCK')
            print('E O J2 ESCOLHEU PAPEL')
            print('J2 GANHOU - SPOCK NAO SABE PREENCHER FORMULARIOS')
            j2+=1
        if pl1==3 and pl2==6:
            print('J1 ESCOLHEU O SPOCK')
            print('E O J2 ESCOLHEU TESOURA')
            print('J1 GANHOU - SPOCK AMASSA TESOURA')
            j1+=1
        if pl1==3 and pl2==9:
            print('J1 ESCOLHEU O SPOCK')
            print('E O J2 ESCOLHEU O LAGARTO')
            print('J2 GANHOU - O LAGARTO ENVENENA O SPOCK')
            j2+=1
        if pl1==4 and pl2==5:
            print('J1 ESCOLHEU O LAGARTO')
            print('E O J2 ESCOLHEU PEDRA')
            print('J2 GANHOU - PEDRA AMASSA O LAGARTO')
            j2+=1
        if pl1==4 and pl2==6:
            print('J1 ESCOLHEU O LAGARTO')
            print('E O J2 ESCOLHEU TESOURA')
            print('J2 GANHOU - TESOURA CORTA A CABEÇA DO LAGARTO')
            j2+=1
        if pl1==4 and pl2==7:
            print('J1 ESCOLHEU O LAGARTO')
            print('E O J2 ESCOLHEU PAPEL')
            print('J1 GANHOU - O LAGARTO COME O PAPEL')
            j1+=1
        if pl1==4 and pl2==8:
            print('J1 ESCOLHEU O LAGARTO')
            print('E O J2 ESCOLHEU O SPOCK')
            print('J1 GANHOU - O LAGARTO ENVENENA O SPOCK')
            j1+=1
        if pl1==0 and pl2==5:
            print('EMPATOU')
            print('OS DOIS ESCOLHERAM O MESMO')
        if pl1==1 and pl2==6:
            print('EMPATOU')
            print('OS DOIS ESCOLHERAM O MESMO')
        if pl1==2 and pl2==7:
            print('EMPATOU')
            print('OS DOIS ESCOLHERAM O MESMO')
        if pl1==3 and pl2==8:
            print('EMPATOU')
            print('OS DOIS ESCOLHERAM O MESMO')
        if pl1==4 and pl2==9:
            print('EMPATOU')
            print('OS DOIS ESCOLHERAM O MESMO')
        j+=1
        print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    if j1>j2:
        print('O SCORE DO JOGADOR 1 FOI:')
        print(j1)
        print('O SCORE DO JOGADOR 2 FOI:')
        print(j2)
        print('O JOGADOR 1 GANHOU')
    if j1<j2:
        print('O SCORE DO JOGADOR 1 FOI:')
        print(j1)
        print('O SCORE DO JOGADOR 2 FOI:')
        print(j2)
        print('O JOGADOR 2 GANHOU')
    if j1==j2:
        print('EMPATOU')
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')