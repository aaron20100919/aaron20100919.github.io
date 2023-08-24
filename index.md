---
layouts: index
---

# aaron0919
aaron0919的博客

<ul>
  {% for post in site.posts %}
    <li class="post">
      <h4><a href="{{ post.url }}">{{ post.title }}</a></h4>
      <p>{{ post.excerpt }}</p>
    </li>
  {% endfor %}
</ul>
