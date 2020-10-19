<template>
    <div class="main-quest">
        <div class="main-quest__container">
            <QuestTree />
        </div>
    </div>
</template>

<script>
import QuestTree from '@/components/QuestTree'
export default {
    name: 'MainQuest',
    components: { QuestTree },
    props: {},
}
</script>

<style lang="scss" scoped>
.main-quest {
    &__container {
        max-width: 1100px;
    }
}
</style>
