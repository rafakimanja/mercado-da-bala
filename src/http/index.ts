import type IMovimentacoes from "@/interface/IMovimentacoes";


export async function obtemTransferencias() { 

    const resposta = await fetch(`http://127.0.0.1:8000/v1/?ordering=-id`)

    const transferencias: IMovimentacoes[] = await resposta.json()

    return transferencias;
}

