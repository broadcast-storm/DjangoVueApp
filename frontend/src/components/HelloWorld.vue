<template>
  <div class="hello">
    <h1>Яндекс Геймификация</h1>
    <div class="article-container">
      <div v-for="article in articles" :key="article.id" class="article">
        <div class="top">
          <h2>{{ article.title }}</h2>
          <div class="img-container">
            <img :src="article.picture" :alt="article.title" />
          </div>
        </div>
        <div class="content-container">
          <p>
            {{
              article.content.length > 250
                ? article.content.slice(0, 250) + "..."
                : article.content
            }}
          </p>
        </div>
        <span>{{
          new Date(article.created_at).getDate() +
            "." +
            new Date(article.created_at).getMonth() +
            "." +
            new Date(article.created_at).getFullYear()
        }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      articles: []
    };
  },
  async mounted() {
    const res = await fetch("/api/articles");
    const articles = await res.json();
    console.log(articles);
    this.articles = articles;
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.article-container {
  width: 100%;
  max-width: 1170px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
.article {
  text-align: center;
  width: 350px;
  margin: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.article .top h2 {
  margin: 15px 0;
}

.article span {
  text-align: left;
  margin-left: 10px;
  font-size: 12px;
  margin-bottom: 10px;
}

.article .content-container {
  min-height: 100px;
}
.article .content-container p {
  text-align: left;
  margin-left: 10px;
}
.article .top img {
  min-width: 100%;
}
.article .top .img-container {
  width: 100%;
  height: 200px;
  overflow: hidden;
  padding: 10px 0;
}
@media (max-width: 800px) {
  .article-container {
    justify-content: center;
  }
}
</style>
