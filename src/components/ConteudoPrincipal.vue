<script lang="ts">
import type IMovimentacoes from '@/interface/IMovimentacoes';
import CardsTransferencia from './CardsTransferencia.vue';

export default{
    components: { CardsTransferencia },
    data(){
        return{
            transferencias: [] as IMovimentacoes[],
            filtros: []
        };
    }
};

</script>

<template>
    <div class="filtros">
        <p>Filtrar por:</p>
        <ul>
            <li><input type="checkbox" value="transferência" v-model="filtros">transferência</li>
            <li><input type="checkbox" value="entrada" v-model="filtros">entrada</li>
            <li><input type="checkbox" value="saída" v-model="filtros">saída</li>
            <li><input type="checkbox" value="banco de reservas" v-model="filtros">banco</li>
        </ul>
    </div>

    <div class="cards-transferencias">
        <CardsTransferencia :filtros="filtros"/>
    </div>
</template>


<style scoped>

.filtros{
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    margin-top: 4rem;
}

.filtros p{
    font-weight: bold;
}

ul{
    display: flex;
    flex-direction: row;
    list-style: none;
}

li{
    display: flex;
    align-items: center;
    margin-right: 10px;
}

.cards-transferencias{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    margin-bottom: 5rem;
    margin-top: 5rem;
}

</style>

