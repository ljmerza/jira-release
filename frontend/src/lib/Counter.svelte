<script lang="ts">
  import { onMount } from 'svelte';

  let bbcode: string = '';
  let toastMessage: string = '';
  let showToast: boolean = false;

  let tickets: any[] = [];
  let JIRA_URL: string = import.meta.env.VITE_API_URL;
  let VITE_FILTER: string = import.meta.env.VITE_FILTER;

  const updateTitle = (ticketKey) => {
    // the fetch and toast methods
  };

  const generateBBCode = () => {
    // logic here
  };

  const copyToClipboard = () => {
    // logic here
  };

  onMount(() => {
    getTickets(VITE_FILTER);
  });

  const getTickets = (filterNumber: string) => {
    fetch(`/filters/${filterNumber}/tickets`)
      .then(response => response.json())
      .then(response => {
          if (response.status === 'success') {
            tickets = response.data;
          } else {
            showToastFn('Error getting tickets.');
          }
      })
      .catch(error => {
        showToastFn('Error: ' + error);
      });
  }

  const showToastFn = (message) => {
    toastMessage = message;
    showToast = true;
    setTimeout(() => {
      showToast = false;
    }, 3000);
  };
</script>

<button on:click={generateBBCode}>Generate BBCode List</button>
<pre class='clipboard'>{bbcode}</pre>
<button on:click={copyToClipboard}>Copy to Clipboard</button>

<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Summary</th>
      <th>Description</th>
      <th>Status</th>
      <th>Assignee</th>
    </tr>
  </thead>
  <tbody>
    {#each tickets as ticket (ticket.key)}
      <tr>
        <td>
          <a href={`${JIRA_URL}/browse/${ticket.key}`} target="_blank">{ticket.key}</a>
        </td>
        <td>
          <input
            data-ticket-id={ticket.key}
            type="text"
            bind:value={ticket.summary}
            
          />
          <button on:click={() => updateTitle(ticket.key)}>Update</button>
        </td>
        <td>{ticket.description}</td>
        <td>{ticket.status}</td>
        <td>{ticket.assignee}</td>
      </tr>
    {/each}
  </tbody>
</table>

<div class='toast' class:show={showToast}>
  {toastMessage}
</div>

<style>
  table {
    width: 100%;
    border-collapse: collapse;
  }

  input {
    width: 80%;
  }

  .toast {
    visibility: hidden;
    max-width: 250px;
    height: 50px;
    line-height: 50px;
    margin-left: -125px;
    background-color: #333;
    color: #fff;
    text-align: center;
    border-radius: 2px;
    position: fixed;
    z-index: 1;
    left: 50%;
    bottom: 30px;
    font-size: 17px;
    padding: 2px 16px;
    transition: visibility 0.5s, opacity 0.5s linear;
    opacity: 0;
  }

  .toast.show {
    visibility: visible;
    opacity: 1;
  }

  .clipboard {
    margin-bottom: 20px;
  }
  
</style>

