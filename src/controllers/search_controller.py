import re

def get_woman_info(phrase: str) -> str:
    '''
    Retorna informações sobre mulheres inspiradoras com base em uma frase.
    
    Args:
        phrase (str): Frase que pode conter o nome de uma mulher pioneira.
                     Ex: "Ada desenvolveu o primeiro algoritmo"
    
    Returns:
        str: Biografia formatada da mulher encontrada ou mensagem inspiradora
             se nenhum nome for encontrado.
    '''
    # Dicionário com padrões regex para cada nome
    name_patterns = {
        'ada lovelace': r'ada(?:\s+lovelace)?(?:\s+adaa)?(?:\s+love)?(?:\s+lovelece)?',
        'grace hopper': r'grace(?:\s+hopper)?(?:\s+holper)?(?:\s+gracee)?',
        'katherine johnson': r'katherine(?:\s+johnson)?(?:\s+jhonsom)?(?:\s+kathrine)?',
        'hedy lamarr': r'hedy(?:\s+lamarr)?(?:\s+lammar)?(?:\s+edi)?',
        'radia perlman': r'radia(?:\s+perlman)?(?:\s+radiaa)?(?:\s+perman)?'
    }

    phrase = phrase.lower()
    
    for name, pattern in name_patterns.items():
        if re.search(pattern, phrase):
            if name == 'ada lovelace':
                return ('🔹 Ada Lovelace\n\n'
                    '💫 Primeira Programadora da História\n\n'
                    '📝 Contribuição:\n'
                    'Escreveu o primeiro algoritmo projetado para ser processado por uma máquina, '
                    'a Máquina Analítica de Charles Babbage.\n\n'
                    '🏆 Legado:\n'
                    'Sua visão pioneira estabeleceu as bases da programação moderna.')
            elif name == 'grace hopper':
                return ('🔹 Grace Hopper\n\n'
                    '💫 Pioneira da Computação\n\n'
                    '📝 Contribuições:\n'
                    '• Criadora da linguagem COBOL\n'
                    '• Popularizou o termo "bug" na computação\n'
                    '• Desenvolveu o primeiro compilador da história\n\n'
                    '🏆 Legado:\n'
                    'Revolucionou a programação tornando-a mais acessível através de linguagens de alto nível.')
            elif name == 'katherine johnson':
                return ('🔹 Katherine Johnson\n\n'
                    '💫 Matemática da NASA\n\n'
                    '📝 Contribuições:\n'
                    '• Cálculos cruciais para missões espaciais\n'
                    '• Trajetórias do Projeto Mercury\n'
                    '• Cálculos para a missão Apollo 11\n\n'
                    '🏆 Legado:\n'
                    'Sua precisão matemática foi fundamental para o sucesso do programa espacial americano.')
            elif name == 'hedy lamarr':
                return ('🔹 Hedy Lamarr\n\n'
                    '💫 Atriz e Inventora\n\n'
                    '📝 Contribuições:\n'
                    '• Sistema de comunicação secreta\n'
                    '• Base para tecnologias Wi-Fi e Bluetooth\n'
                    '• Patente de espectro amplo\n\n'
                    '🏆 Legado:\n'
                    'Suas invenções revolucionaram as comunicações sem fio modernas.')
            elif name == 'radia perlman':
                return ('🔹 Radia Perlman\n\n'
                    '💫 A "Mãe da Internet"\n\n'
                    '📝 Contribuições:\n'
                    '• Desenvolvimento do Spanning Tree Protocol\n'
                    '• Pioneira em redes de computadores\n'
                    '• Mais de 100 patentes registradas\n\n'
                    '🏆 Legado:\n'
                    'Seus protocolos são fundamentais para o funcionamento da internet atual.')

    return ('💜 Para todas as mulheres que sonham alto:\n\n'
            '🌟 Inspiração\n'
            'Vocês têm dentro de si a força para transformar o mundo. '
            'Cada passo que dão é uma inspiração para outras seguirem seus próprios caminhos.\n\n'
            '💪 Força\n'
            'Não deixem que ninguém limite seu potencial – suas ideias, sua voz e suas conquistas importam!\n\n'
            '✨ Mensagem\n'
            'Seja na tecnologia, na ciência, nas artes ou em qualquer área, '
            'o lugar de vocês é onde quiserem estar.\n\n'
            '🚀 Lembre-se:\n'
            'Você é capaz de realizar coisas extraordinárias!')

# Testes
if __name__ == '__main__':
    frases_teste = [
        "Ada Lovelace foi incrível",
        "Grace Murray desenvolveu o COBOL",
        "Katherine calculou trajetórias espaciais",
        "Hedy inventou tecnologias sem fio",
        "Radia criou protocolos importantes",
        "Carla não está na lista"
    ]

    for frase in frases_teste:
        print(f"\nTestando: {frase}")
        print("-" * 50)
        print(get_woman_info(frase))
