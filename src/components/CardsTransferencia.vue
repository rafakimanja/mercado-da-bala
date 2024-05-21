<script lang="ts">
import { obtemTransferencias } from '@/http';
import type IMovimentacoes from '@/interface/IMovimentacoes';
export default{
    data(){
        return{
            transferencias: [] as IMovimentacoes[]
        }
    },
     async created(){
         this.transferencias = await obtemTransferencias();
    },
    props: {
        filtros: {
            type: Array,
            required: true
        }
    },
    computed: {
        transferenciasFiltradas: function(){
            if(this.filtros.length > 0){
                return this.transferencias.filter(transferencia => this.filtros.includes(transferencia.movimentacao))
            }else{
                return this.transferencias
            }
        }
    }
}

</script>

<template>
    <div class="transferencias">
        <table>
            <tr>
                <th>Jogador</th>
                <th>Movimentação</th>
                <th>Origem</th>
                <th>Destino</th>
            </tr>
            <tr v-for="transferencia in transferenciasFiltradas" :key="transferencia.id">
                <td>{{ transferencia.nome }}</td>
                <td>{{ transferencia.movimentacao }}</td>
                <td>{{ transferencia.origem }}</td>
                <td>{{ transferencia.destino }}</td>
            </tr>
        </table>
    </div>
</template>



<style scoped>
.transferencias{
    width: 800px;
    margin-bottom: 2rem;
    text-align: center;
}

.card-transferencia span{
    font-weight: bold;
}

table{
    border-collapse: collapse;
    width: 100%;
}

td, th{
    border: 1px solid #E38617;
    padding: 8px;
}
</style>